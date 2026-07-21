from http.client import HTTPResponse
from django.shortcuts import render,get_object_or_404,redirect
from carts.models import CartItem
from .forms import ReviewForm
from .models import Product, ReviewRating
from category.models import Category
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


def store(request, category_slug=None):
    categories=None
    products = None

    if category_slug!=None:
        categories=get_object_or_404(Category, slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        # Fetching the specific product
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    # Initialize an empty products list in case the keyword is blank
    products = []
    product_count = 0

    # 1. Check if the URL has a '?keyword=' in it
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')

        # 2. If the user actually typed something (not just empty spaces)
        if keyword:
            # 3. Query the database using Q objects
            products = Product.objects.filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            ).order_by('-created_date')

            product_count = products.count()

    # 4. We reuse the exact same store.html template!
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')

    # Check if the URL exists, default to the homepage if someone accesses the route directly
    if not url:
        url = '/'

    if request.method == "POST":
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank You! Your Review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank You! Your Review has been submitted.')
                return redirect(url)

    # FIXED: Added a fallback return statement so the view never returns None
    return redirect(url)







from django.contrib.auth import authenticate

from . models import Cart, CartItem
from carts.views import _cart_id

from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:

            # --- THE FIX: Check authentication FIRST ---
            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user=request.user)
            else:
                # Only look for a session cart if they are a guest
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart)
            # -----------------------------------------

            for cart_item in cart_items:
                cart_count += cart_item.quantity

        except Cart.DoesNotExist:
            cart_count = 0

    return dict(cart_count=cart_count)

<h1>GreatKart 🛒</h1>
GreatKart is a fully functional, feature-rich e-commerce web application built using Python and Django. It provides a complete shopping experience from product browsing and cart management to secure checkout, order tracking, and product reviews.

<h3>🚀 Key Features</h3>
<b>Custom User Authentication:</b> Secure login, registration, and user dashboard using a custom Django user model.

<b>Product Catalog & Categories:</b> Dynamic product listings with category filtering and pagination.

<b>Product Variations:</b> Support for multiple product attributes (e.g., Size, Color) with precise cart management.

<b>Smart Shopping Cart:</b> Session-based cart functionality with quantity adjustments and real-time subtotal/tax calculations.

<b>Search Functionality:</b> Keyword-based search across product names and descriptions.

<b>Secure Checkout & Orders:</b> 
<ul>
<li>Generation of unique order numbers and transaction IDs.</li>

<li>Historical price freezing (saves the exact price of an item at the moment of checkout).</li>

<li>Post-checkout visual invoices and order history.</li>
</ul>

<b>Rating & Reviews:</b> Users can leave star ratings and text reviews for products they have purchased.

<b>Admin Dashboard:</b> Powerful Django admin interface to manage inventory, categories, orders, and users.

<h3>🛠️ Tech Stack</h3>
<b>Backend:</b> Python 3, Django

<b>Frontend:</b> HTML5, CSS3, Bootstrap (Responsive UI)

<b>Database:</b> SQLite (Development) / PostgreSQL (Production ready)

<h3>📂Complete Project File Structure</h3>

Below is the complete directory tree of the GreatKart e-commerce platform, illustrating the separation of Django apps, static assets, media storage, and HTML templates:

```text
GreatKart/
│
├── accounts/                  # User authentication & profile management app
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py              # Custom User Model & UserProfile
│   ├── urls.py
│   └── views.py               # Login, register, activation & dashboard logic
│
├── carts/                     # Shopping cart math & session logic app
│   ├── migrations/
│   ├── context_processors.py  # Global cart item counter for navbar
│   ├── models.py              # Cart & CartItem database models
│   ├── urls.py
│   └── views.py               # Add, remove, and decrement cart item logic
│
├── category/                  # Product category management app
│   ├── migrations/
│   ├── context_processors.py  # Global category dropdown menu loader
│   ├── models.py              # Category model with custom slug URLs
│   └── views.py
│
├── GreatKart/                 # Inner core project configuration folder
│   ├── static/                # Core static overrides
│   ├── asgi.py
│   ├── settings.py            # Main project configuration & database connection
│   ├── urls.py                # Master URL routing controller
│   ├── views.py               # Global views (e.g., Homepage rendering)
│   └── wsgi.py                # Production web server gateway interface
│
├── media/                     # User-uploaded content & product catalogs
│   └── photos/
│       ├── category/          # Category display banners
│       └── products/          # Individual product images
│
├── orders/                    # Checkout, payments & invoice handling app
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py               # Shipping address capture form
│   ├── models.py              # Order, OrderProduct, and Payment models
│   ├── urls.py
│   └── views.py               # PayPal gateway processing & receipt rendering
│
├── static/                    # Global front-end static assets
│   ├── admin/                 # Custom admin stylesheet overrides
│   ├── css/                   # Stylesheets for storefront layout
│   ├── fonts/                 # Custom web fonts
│   ├── images/                # Static UI logos, icons, and banners
│   └── js/                    # Client-side JavaScript & interactive scripts
│
├── store/                     # Storefront catalog & review management app
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py               # Review & rating submission form
│   ├── models.py              # Product, Variation, and ReviewRating models
│   ├── urls.py
│   └── views.py               # Search engine & category filtering logic
│
├── templates/                 # Global HTML visual templates
│   ├── accounts/              # Auth UI (login, register, reset password, dashboard)
│   ├── includes/              # Reusable components (navbar, footer, alerts)
│   ├── orders/                # Payment page & order confirmation invoices
│   └── store/                 # Main storefront (home, base layout, product detail)
│
├── .gitignore                 # Specifies intentionally untracked files for Git
├── db.sqlite3                 # Local SQLite development database
├── manage.py                  # Django command-line execution utility
├── README.md                  # Project documentation & visual walkthrough
└── requirements.txt           # Python package dependency list

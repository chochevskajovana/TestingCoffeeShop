"""
URL configuration for DNICKproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from CoffeeShop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('products/', products, name="products"),
    path('add_new/', add_new, name="add_new"),
    path('coffee/edit/<int:id>', add_new, name='edit_coffee'),
    path('delete/<int:id>', delete_coffee, name="delete_coffee"),
    path('search_feature/', search_feature, name='search_feature'),
    path('add_to_cart/', add_to_cart, name="add_to_cart"),
    path('cart/', cart, name="cart"),
    path('cart_empty/', cart_empty, name="cart_empty"),
    path('increase_quantity/<int:id>', increase_quantity, name="increase_quantity"),
    path('decrease_quantity/<int:id>', decrease_quantity, name="decrease_quantity"),
    path('increase_servings/<int:id>', increase_servings, name="increase_servings"),
    path('decrease_servings/<int:id>', decrease_servings, name="decrease_servings"),
    path('orders/', orders, name="orders"),
    path('delete_order_item/<int:id>', delete_order_item, name="delete_order_item"),
    path('delete_order/<int:id>', delete_order, name='delete_order'),
    path('login/', loginUser, name="login"),
    path('register/', register, name="register"),
    path('logout/', logoutUser, name='logoutUser'),
    path('checkOut/', check_out, name="check_out"),
    path('confirmation/', confirmation, name="confirmation"),
    path('not_allowed/', not_allowed, name='not_allowed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

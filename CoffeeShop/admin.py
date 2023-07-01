from django.contrib import admin

from CoffeeShop.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Flavours)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Checkout)

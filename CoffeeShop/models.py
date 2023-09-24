from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Flavours(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.user.username} - {str(self.id)}"

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    # @property
    # def get_cart_items(self):
    #     order_items = self.orderitem_set.all()
    #     total = sum([item.quantity for item in order_items])
    #     return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    coffee = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    additional_flavor = models.ForeignKey(Flavours, on_delete=models.CASCADE, null=True)
    servings = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coffee} - {self.quantity}"

    @property
    def get_total(self):
        total_coffee = self.coffee.price * self.quantity
        total_flavor = self.additional_flavor.price * self.servings
        total = total_coffee + total_flavor
        return total


class Checkout(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    surname = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.address} : {self.order.id}"

from django.test import TestCase
from django.contrib.auth.models import User
from CoffeeShop.models import *


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jovana', password='1wax2qsz')
        self.customer = Customer.objects.create(user=self.user, email='jovana.chochevska@gmail.com')
        self.product = Product.objects.create(name='Cappuccino', price=20, image='../images/products/cappuchino.png')
        self.flavour = Flavours.objects.create(name='Chocolate', price=3)
        self.order = Order.objects.create(customer=self.customer, date_ordered=10.07, complete=True)
        self.orderItem1 = OrderItem.objects.create(order=self.order, coffee=self.product, quantity=3,
                                                   additional_flavor=self.flavour, servings=1)
        self.orderItem2 = OrderItem.objects.create(order=self.order, coffee=self.product, quantity=4,
                                                   additional_flavor=self.flavour, servings=2)
        self.checkOut = Checkout.objects.create(customer=self.customer, order=self.order, name="Jovana",
                                                surname="Chochevska", email="jovana.chochevska.com",
                                                address="Nikola Tesla", phone="123456789")

    def test_customer_model(self):
        self.assertEqual(str(self.customer), "jovana")

    def test_product_model(self):
        self.assertEqual(str(self.product), "Cappuccino")

    def test_flavour_model(self):
        self.assertEqual(str(self.flavour), "Chocolate")

    def test_order_model(self):
        self.assertEqual(str(self.order), str(self.customer.user.username) + " - " + str(self.order.id))

    def test_orderItem_model(self):
        self.assertEqual(str(self.orderItem1), "Cappuccino - 3")

    def test_checkOut_model(self):
        self.assertEqual(str(self.checkOut), "Jovana - Nikola Tesla : " + str(self.order.id))

    def test_get_total_price(self):
        coffee_price1 = self.product.price * self.orderItem1.quantity
        flavour_price1 = self.flavour.price * self.orderItem1.servings
        total_price = coffee_price1 + flavour_price1
        self.assertEqual(self.orderItem1.get_total, total_price)

    def test_get_cart_total(self):
        coffee_price1 = self.product.price * self.orderItem1.quantity
        flavour_price1 = self.flavour.price * self.orderItem1.servings
        coffee_price2 = self.product.price * self.orderItem2.quantity
        flavour_price2 = self.flavour.price * self.orderItem2.servings
        total_price = coffee_price1 + flavour_price1 + coffee_price2 + flavour_price2
        self.assertEqual(self.order.get_cart_total, total_price)

from django.test import TestCase
from django.urls import reverse
from CoffeeShop.models import *
from django.contrib.auth.models import Group


class TestDefaultViews(TestCase):

    def test_home_view(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_default_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_products_view(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def test_cart_view(self):
        self.client.post('/login/', {'username': 'admin', 'password': '201107superuser'})
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=%2Fcart%2F')

    def test_cart_empty_view(self):
        self.client.post('/login/', {'username': 'admin', 'password': '201107superuser'})
        response = self.client.get('/cart_empty/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=%2Fcart_empty%2F')


class TestSearchFeature(TestCase):

    def test_search_feature_view(self):
        response = self.client.get("/search_feature/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def test_search_feature_valid(self):
        response = self.client.post('/search_feature/', {'search_query': 'Cappuccino'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def test_search_feature_invalid(self):
        response = self.client.post('/search_feature/', {'search_query': 'Nonexistent Coffee'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')


class TestAuthenticationViews(TestCase):

    def test_logout_view(self):
        self.client.login(username='admin', password='superuser')
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/logout/')

    def test_login_view(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_view(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_not_allowed_view(self):
        response = self.client.get("/not_allowed/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'not_allowed.html')

    def test_login_user_valid(self):
        response = self.client.post('/login/', {'username': 'admin', 'password': '201107superuser'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_user_invalid(self):
        response = self.client.post('/login/', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_user_valid(self):
        Group.objects.create(name='customer')
        response = self.client.post('/register/', {'username': 'new_user1', 'password1': 'new_Password1234',
                                                   'password2': 'new_Password1234'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_register_user_invalid(self):
        response = self.client.post('/register/', {'username': '', 'password1': 'password', 'password2': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class TestCartViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, email='test@example.com')
        self.product = Product.objects.create(name='Test Product', price=10)
        self.flavor = Flavours.objects.create(name='Test Flavor', price=5)
        self.order = Order.objects.create(customer=self.customer, complete=False)
        self.order_item = OrderItem.objects.create(order=self.order, coffee=self.product, quantity=2,
                                                   additional_flavor=self.flavor, servings=1)
        self.checkout = Checkout.objects.create(customer=self.customer, order=self.order, name='Test Name',
                                                surname='Test Surname', email='test@example.com',
                                                address='Test Address', phone='123456789')
        self.client.post('/login/', {'username': 'admin', 'password': '201107superuser'})

    def test_add_to_cart(self):
        response = self.client.post('/add_to_cart/', {'coffee_id': 3})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url="/login/?next=%2Fadd_to_cart%2F")

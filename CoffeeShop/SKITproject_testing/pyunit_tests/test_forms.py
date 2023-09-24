from django.test import TestCase
from django.contrib.auth.models import User
from CoffeeShop.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile
from CoffeeShop.forms import CreateUserForm, CoffeeForm


class CreateUserFormTest(TestCase):
    def test_create_user_form_valid_data(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_user_form_invalid_data(self):
        # Test with invalid data (passwords don't match)
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword1',
            'password2': 'testpassword2',
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())


class CoffeeFormTest(TestCase):
    def test_coffee_form_valid_data(self):
        form_data = {
            'name': 'Test Coffee',
            'price': 5,
            'quantity': 10,
        }
        form = CoffeeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_coffee_form_invalid_data(self):
        # Test with negative quantity
        form_data = {
            'name': 'Test Coffee',
            'price': 5.99,
            'quantity': -10,  # Negative quantity, which is invalid based on the model's field constraint.
        }
        form = CoffeeForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test with non-integer price
        form_data = {
            'name': 'Test Coffee',
            'price': 'invalid_price',  # Price is given as a string, should be an integer.
            'quantity': 10,
        }
        form = CoffeeForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test with invalid image file format (only valid image formats: jpg, jpeg, png, gif)
        invalid_image = SimpleUploadedFile("test.txt", b"invalid_image_data")
        form_data = {
            'name': 'Test Coffee',
            'price': 5.99,
            'quantity': 10,
            'image': invalid_image,
        }
        form = CoffeeForm(data=form_data, files={'image': invalid_image})
        self.assertFalse(form.is_valid())

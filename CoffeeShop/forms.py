from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from CoffeeShop.models import Product


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control mb-3"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


class CoffeeForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput())

    def __init__(self, *args, **kwargs):
        super(CoffeeForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control mb-3"

    class Meta:
        model = Product
        fields = '__all__'

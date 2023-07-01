from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from CoffeeShop.decorators import allowed_users, unauthenticated_user, user_passes_test
from CoffeeShop.forms import CreateUserForm, CoffeeForm
from CoffeeShop.models import *


def home(request):
    return render(request, "home.html")


def products(request):
    coffees = Product.objects.all()

    p = Paginator(coffees, 12)
    page_num = request.GET.get('page', 1)

    coffee_names = ['Cappuccino', 'Espresso', 'Cortado', 'Macchiato', 'Irish coffee', 'Flat white', 'Affogato',
                    'Americano', 'Iced coffee', 'Nescafe', 'Frappuchino', 'Hot chocolate']
    flavour_names = ['Chocolate', 'Vanilla', 'Strawberry', 'Caramel']

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {'coffees': page, 'coffee_names': coffee_names, 'flavour_names': flavour_names}
    return render(request, "products.html", context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['seller'])
def add_new(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = CoffeeForm(request.POST, request.FILES)
        else:
            coffee = Product.objects.get(pk=id)
            form = CoffeeForm(request.POST, request.FILES, instance=coffee)
        if form.is_valid():
            form.save()
        return redirect("products")
    else:
        if id == 0:
            form = CoffeeForm()
        else:
            coffee = Product.objects.get(pk=id)
            form = CoffeeForm(instance=coffee)

    context = {"form": form}
    return render(request, "add_new.html", context=context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['seller'])
def delete_coffee(request, id=0):
    coffee = Product.objects.get(pk=id)
    coffee.delete()
    return redirect('products')


def search_feature(request):
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST.get('search_query')
        print(search_query)
        print("test")
        # Filter your model by the search query
        coffees = Product.objects.filter(name__contains=search_query)
        return render(request, 'products.html', {'query': search_query, 'coffees': coffees})
    else:
        return render(request, 'products.html', {})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def add_to_cart(request, id=0):
    if request.method == 'POST':
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            coffee_id = request.POST.get('coffee_id')
            coffee = get_object_or_404(Product, pk=coffee_id)
            order_item_exists = order.orderitem_set.filter(coffee=coffee).first()

            if order_item_exists:
                order_item = order_item_exists
                order_item.quantity += 1
                order_item.save()
            else:
                order_item = OrderItem.objects.create(coffee=coffee, order=order, quantity=1,
                                                      additional_flavor=Flavours.objects.all()[0], servings=0)
                order_item.save()

        return redirect('cart')
    else:
        return redirect('products')


def is_superuser(user):
    return user.is_superuser


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def cart(request):
    flavours = Flavours.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        if len(items) == 0:
            return redirect('cart_empty')
    else:
        items = []
        order = {'get_cart_total': 0}

    context = {'items': items, 'order': order, 'flavours': flavours}
    return render(request, "cart.html", context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def cart_empty(request):
    return render(request, "cart_empty.html")


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def increase_quantity(request, id):
    order_item = OrderItem.objects.get(pk=id)
    order_item.quantity += 1
    order_item.save()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def decrease_quantity(request, id):
    order_item = OrderItem.objects.get(pk=id)
    if order_item.quantity <= 1:
        order_item.quantity = 1
    else:
        order_item.quantity -= 1
    order_item.save()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def increase_servings(request, id):
    order_item = OrderItem.objects.get(pk=id)
    order_item.servings += 1
    order_item.save()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def decrease_servings(request, id):
    order_item = OrderItem.objects.get(pk=id)
    if order_item.servings <= 1:
        order_item.servings = 1
    else:
        order_item.servings -= 1
    order_item.save()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['seller'])
def orders(request):
    all_orders = Checkout.objects.all()
    context = {'all_orders': all_orders}
    return render(request, "orders.html", context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['seller', 'customer'])
def delete_order_item(request, id=0):
    order_item = OrderItem.objects.get(pk=id)
    order_item.delete()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def delete_order(request, id=0):
    order_to_delete = Checkout.objects.get(pk=id)
    order_to_delete.delete()
    return redirect('orders')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def check_out(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        if request.method == "POST":

            order.complete = True
            order.save()

            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            surname = ""
            email = ""

            check_out_order = Checkout()
            check_out_order.customer = customer
            check_out_order.order = order
            check_out_order.name = name
            check_out_order.surname = surname
            check_out_order.email = email
            check_out_order.address = address
            check_out_order.phone = phone
            check_out_order.save()
            return redirect('confirmation')
    else:
        items = []
        order = {'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, "check_out.html", context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def confirmation(request):
    return render(request, "confirmation.html")


@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Bad credentials')

    context = {}
    return render(request, "login.html", context=context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    customer = Customer()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            customer.user = user
            customer.email = user.email
            customer.save()

            messages.add_message(request, messages.SUCCESS, 'Account was created for ' + user.username)
            return redirect('login')

    context = {"form": form}
    return render(request, "register.html", context=context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')


def not_allowed(request):
    return render(request, 'not_allowed.html')

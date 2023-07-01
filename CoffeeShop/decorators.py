from functools import wraps

from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('not_allowed')

        return wrapper_func

    return decorator


def seller_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('home')

        if group == 'seller':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def user_passes_test(test_func, login_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            return redirect(login_url or 'loginPage')
        return wrapped_view
    return decorator


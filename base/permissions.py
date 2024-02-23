from django.shortcuts import redirect, render
from functools import wraps


def technician_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_technician:
            return function(request, *args, **kwargs)
        else:
            return render(request, "forbidden.html")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def customer_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_customer and request.user.is_active:
            return function(request, *args, **kwargs)
        else:
            return render(request, "forbidden.html")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            return render(request, "forbidden.html")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

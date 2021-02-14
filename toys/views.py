from django.shortcuts import render

from toys.models import User, Toy


def dashboard(request):
    return render(request, "toys/dashboard.html", context={"text": "Welcome to AllToys!"})


def show_toys(request):
    toys = Toy.objects.all()
    return render(request, "toys/show_toys.html", context={"toys": toys})


def show_users(request):
    users = User.objects.all()
    return render(request, "toys/show_users.html", context={"users": users})

def get_toy_detail(request, **kwargs):
    try:
        toy = Toy.objects.get(pk = kwargs.get("id"))
    except Exception:
        return render(request, "toys/error.html", context={"error_text": "This Toy does not exist!"})

    return render(request, "toys/toy_detail.html", context={"toys": toy})


def error(request):
    return None
from django.shortcuts import render

from toys.models import User, Toy


def dashboard(request):
    return render(request, "toys/dashboard.html", context={"Welcome_text": "Welcome bitch!"})


def show_toys(request):
    toys = Toy.objects.all()
    return render(request, "toys/show_toys.html", context={"toys": toys})


def show_users(request):
    users = User.objects.all()
    return render(request, "toys/show_users.html", context={"users": users})

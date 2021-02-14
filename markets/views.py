from django.shortcuts import render

from markets.models import Markets


def dashboard(request):
    return render(request, "markets/dashboard.html", context={"text": "Welcome to Markets!"})

def show_markets(request):
    markets = Markets.objects.all()
    return render(request, "markets/show_markets.html", context={"markets": markets})
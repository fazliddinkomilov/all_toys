from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView
from markets.models import Markets

class DashboardView(TemplateView):
    template_name = "markets/dashboard.html"
    extra_context = {"text": "Welcome to Markets!"}

class Show_markets(TemplateView):
    markets = Markets.objects.all()
    template_name = "markets/show_markets.html"
    extra_context = {"markets": markets}

class Markets_list_view(ListView):
    model = Markets
    template_name = "markets/show_markets.html"
    queryset = Markets.objects.filter()

    # def get_queryset(self):
    #     market = Markets.objects.filter(created_at__year=timezone.now().year)
    #     return market

class Market_Detail_View(DetailView):
    model = Markets
    template_name = "markets/markets_detail.html"

#
# def gey_market_detail(request, **kwargs):
#     try:
#         market = Markets.objects.get(pk=kwargs.get("id"))
#     except Exception:
#         return render(request, "toys/error.html", context={"error_text": "This Toy does not exist!"})
#
#     return render(request, "markets/markets_detail.html", context={"markets": market})
#

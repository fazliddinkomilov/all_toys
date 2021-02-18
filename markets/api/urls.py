from django.urls import path

from markets import views

app_name = "markets"
urlpatterns = [
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('markets/', views.Markets_list_view.as_view(), name="markets"),
    path('markets/<int:pk>', views.Market_Detail_View.as_view(), name="market_detail"),
]
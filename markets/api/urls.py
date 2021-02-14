from django.urls import path

from markets import views

app_name = "markets"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('markets/', views.show_markets, name="markets"),
]
from django.urls import path
from . import views

app_name = "toys"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('toys', views.show_toys, name="toys"),
    path('users', views.show_users, name="users"),


]
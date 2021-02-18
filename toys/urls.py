from django.urls import path
from toys import views

app_name = "toys"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('toys/', views.show_toys, name="toys"),
    path('users/', views.show_users, name="users"),
    path('error/', views.error, name="error"),
    path('toys/<int:id>', views.get_toy_detail, name="toy_detail"),


]
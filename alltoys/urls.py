from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', include(("toys.urls","toys"))),
    path('admin/', admin.site.urls),
]

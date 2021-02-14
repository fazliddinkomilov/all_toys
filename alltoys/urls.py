from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('toys/', include('toys.urls', namespace="toys")),
    path('markets/', include('markets.api.urls', namespace="markets")),
    path('admin/', admin.site.urls),
]

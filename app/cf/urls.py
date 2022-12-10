from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("inventory.urls", namespace="inventory")),
    path("admin/", admin.site.urls),
]

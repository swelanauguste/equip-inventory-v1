from django.urls import path

from .views import (
    EquipmentCreateView,
    EquipmentDeleteView,
    EquipmentDetailView,
    EquipmentListView,
    EquipmentUpdateView,
)

app_name = "inventory"

urlpatterns = [
    path("", EquipmentListView.as_view(), name="equip-list"),
    path("detail/<int:pk>/", EquipmentDetailView.as_view(), name="equip-detail"),
    path("create/", EquipmentCreateView.as_view(), name="equip-create"),
    path("update/<int:pk>/", EquipmentUpdateView.as_view(), name="equip-update"),
    path("delete/<int:pk>/", EquipmentDeleteView.as_view(), name="equip-delete"),
]

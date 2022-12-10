from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Category, Equipment, Owner
from .forms import EquipmentCreateForm

class EquipmentListView(ListView):
    model = Equipment


class EquipmentDetailView(DetailView):
    model = Equipment


class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentCreateForm


class EquipmentUpdateView(UpdateView):
    model = Equipment
    form_class = EquipmentCreateForm


class EquipmentDeleteView(DeleteView):
    model = Equipment

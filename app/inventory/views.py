import socket

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import EquipmentCreateForm
from .models import Category, Equipment, Owner
from .filters import EquipmentFilter

class EquipmentListView(ListView):
    paginate_by = 25
    model = Equipment
    
    # queryset = Equipment.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EquipmentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


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

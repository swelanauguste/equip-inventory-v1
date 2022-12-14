import django_filters

from .models import Equipment


class EquipmentFilter(django_filters.FilterSet):
    
    serial_number = django_filters.CharFilter(lookup_expr='icontains')
    make_model = django_filters.CharFilter(lookup_expr='icontains')
    owner__name = django_filters.CharFilter(lookup_expr='icontains')
  
    class Meta:
        model = Equipment
        fields = ['category', 'serial_number', "make_model", 'owner__name']
      
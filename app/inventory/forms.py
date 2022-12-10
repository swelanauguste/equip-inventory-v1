from django import forms

from .models import Category, Equipment, Owner


class EquipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"
        widgets = {
            "date_received": forms.TextInput(attrs={"type": "date"}),
            "date_issued": forms.TextInput(attrs={"type": "date"}),
        }

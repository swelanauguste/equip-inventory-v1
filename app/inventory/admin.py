from django.contrib import admin

from .models import Category, Equipment, Owner

admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Owner)

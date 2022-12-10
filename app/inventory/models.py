from django.db import models
from django.urls import reverse

class Owner(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category.title()


class Equipment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100, unique=True)
    make_model = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name="equipment_list"
    )
    date_received = models.DateField()
    date_issued = models.DateField()

    class Meta:
        ordering = ("-date_issued",)
        verbose_name_plural = "equipment"

    def get_absolute_url(self):
        return reverse("inventory:equip-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.make_model} issued to {self.owner.name} on {self.date_issued}"

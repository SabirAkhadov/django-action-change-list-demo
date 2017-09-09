from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, default="Electronics")


class Sale(models.Model):
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(default=0, max_digits=1000000, decimal_places=2)
    category = models.ForeignKey(to=Category, related_name='sales', null=True)


class SaleSummary(Sale):
    class Meta:
        proxy = True
        verbose_name = "Sale Summary"
        verbose_name_plural = "Sales Summary"

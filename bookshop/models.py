from django.db import models
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=160)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        verbose_name = ' Товар '
        verbose_name_plural = ' Товары '

    def __str__(self):
        return f'{self.name}'

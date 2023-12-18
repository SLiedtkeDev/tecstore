from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Nombre', null=False, blank=False)
    description = models.CharField(
        max_length=300, verbose_name='Descripcion', null=False, blank=False)
    price = models.FloatField(verbose_name='Costo Unitario')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def __str__(self):
        return self.name

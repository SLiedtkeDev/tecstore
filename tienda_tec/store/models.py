from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Nombre', null=False, blank=False)
    description = models.CharField(
        max_length=300, verbose_name='Descripcion', null=False, blank=False)
    price = models.FloatField(verbose_name='Costo Unitario')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    stock = models.IntegerField(verbose_name='Cantidad')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def __str__(self):
        return self.name


class Order(models.Model):
    email = models.EmailField(verbose_name='Email')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    neighborhood = models.CharField(max_length=200, verbose_name='Colonia')
    total = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Total')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-created']

    def __str__(self):
        return self.emails

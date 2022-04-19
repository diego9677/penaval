from django.db import models
from django.contrib.auth.models import User
from registration.models import Cliente
from productos.models import Producto


class Venta(models.Model):
    usuario = models.ForeignKey(User, related_name='ventas', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='ventas', on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Emisión')
    productos = models.ManyToManyField(Producto, related_name='ventas', through='DetalleVenta')

    def __str__(self):
        return self.fecha_emision.strftime('%d/%m/%Y %H:%M:%S')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio Unitario')
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Subtotal')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'


class Proforma(models.Model):
    usuario = models.ForeignKey(User, related_name='proformas', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='proformas', on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Emisión')
    productos = models.ManyToManyField(Producto, related_name='proformas', through='DetalleProforma')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Proforma'
        verbose_name_plural = 'Proformas'


class DetalleProforma(models.Model):
    proforma = models.ForeignKey(Proforma, related_name='detalle_proforma', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio Unitario')
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Subtotal')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Detalle de la proforma'
        verbose_name_plural = 'Detalles de las proformas'

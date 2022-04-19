from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto


class Proveedor(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    direccion = models.TextField(verbose_name='Dirección')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Compra(models.Model):
    usuario = models.ForeignKey(
        User, related_name='compras', on_delete=models.CASCADE)
    proveedor = models.ForeignKey(
        Proveedor, related_name='compras', on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Emisión')
    productos = models.ManyToManyField(
        Producto, related_name='compras', through='DetalleCompra')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio_unitario_compra = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Precio Unitario Compra')
    precio_unitario_venta = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Precio Unitario Venta')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalle de Compras'

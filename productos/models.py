from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(
        blank=True, null=True, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Lugar(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(
        blank=True, null=True, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'


class Producto(models.Model):
    codigo = models.CharField(
        max_length=100, unique=True, verbose_name='Código')
    lugar = models.ForeignKey(
        Lugar, related_name='productos', on_delete=models.CASCADE)
    marca = models.ForeignKey(
        Marca, related_name='productos', on_delete=models.CASCADE)
    cantidad_disponible = models.PositiveIntegerField(
        default=0, verbose_name='Cantidad Disponible')
    precio_unitario = models.DecimalField(
        default=0, max_digits=9, decimal_places=2,
        verbose_name='Precio Unitario')
    medidas = models.CharField(max_length=255, verbose_name='Medidas')

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

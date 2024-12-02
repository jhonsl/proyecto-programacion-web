from django.db import models

# Crear un modelo para Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del producto
    categoria = models.CharField(max_length=100)  # Categoría del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio con decimales
    cantidad_en_stock = models.IntegerField()  # Cantidad disponible en inventario
    fecha_agregado = models.DateField()  # Fecha en que el producto fue agregado

    def __str__(self):
        return f"{self.nombre} - {self.categoria} ({self.precio})"
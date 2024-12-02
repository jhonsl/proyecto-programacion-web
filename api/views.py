from rest_framework import viewsets
from .models import Producto
from .serial import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # Queryset que define los datos que se mostrarán en las vistas
    queryset = Producto.objects.all()
    
    # El serializador que se utilizará para convertir los datos a JSON
    serializer_class = ProductoSerializer
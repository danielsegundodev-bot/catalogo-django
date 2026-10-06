from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductoSerializer

    # Punto 5: Consulta con Django ORM
    @action(detail=False, methods=['get'], url_path='disponibles')
    def disponibles(self, request):
        # El requerimiento pide resolverlo con el ORM de Django
        productos_disponibles = Producto.objects.filter(activo=True, stock__gt=0)
        serializer = self.get_serializer(productos_disponibles, many=True)
        return Response(serializer.data)
import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
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

@api_view(['GET'])
def consumo_api_externa(request):
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    
    try:
        # Timeout explícito de 5 segundos, como pide el requerimiento
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Lanza excepción si el código HTTP es de error
        
        datos = response.json()
        return Response({"mensaje": "Datos obtenidos correctamente", "data": datos}, status=status.HTTP_200_OK)
        
    except requests.exceptions.Timeout:
        return Response({"error": "La petición a la API externa tardó demasiado (Timeout)."}, status=status.HTTP_504_GATEWAY_TIMEOUT)
    except requests.exceptions.ConnectionError:
        return Response({"error": "Fallo de conexión con la API externa."}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except requests.exceptions.RequestException as e:
        return Response({"error": f"Error inesperado al consultar la API: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
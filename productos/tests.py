from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Producto

class ProductoAPITestCase(APITestCase):

    def setUp(self):
        self.url = '/api/productos/'

    def test_crear_producto_valido(self):
        """Verifica que se pueda crear un producto correctamente."""
        data = {
            "nombre": "Teclado Mecánico",
            "descripcion": "Switch Red RGB",
            "precio": "79.99",
            "stock": 10,
            "activo": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 1)
        self.assertEqual(Producto.objects.get().nombre, "Teclado Mecánico")

    def test_rechazar_precio_negativo(self):
        """Verifica que la API rechace un precio menor o igual a 0."""
        data = {
            "nombre": "Mouse Gamer",
            "precio": "-15.00",
            "stock": 5,
            "activo": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
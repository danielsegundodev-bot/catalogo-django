from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, consumo_api_externa

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')

urlpatterns = [
    path('', include(router.urls)),
    path('externa/', consumo_api_externa, name='api_externa'),
]
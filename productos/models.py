from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    # Obligatorio, máximo 150 caracteres
    nombre = models.CharField(max_length=150, null=False, blank=False)
    
    # Opcional
    descripcion = models.TextField(blank=True, null=True)
    
    # Debe ser mayor que 0
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    
    # No puede ser negativo
    stock = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    
    # Valor inicial True
    activo = models.BooleanField(default=True)
    
    # Asignación automática al crear
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
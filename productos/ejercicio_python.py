def filtrar_y_ordenar_productos(productos):
    # 1. Filtrar productos con stock > 0
    # 2. Ordenar por la clave 'precio' de menor a mayor
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    return sorted(productos_disponibles, key=lambda x: x['precio'])

# Bloque de prueba
if __name__ == '__main__':
    productos_ejemplo = [
        {'nombre': 'A', 'precio': 100, 'stock': 0},
        {'nombre': 'B', 'precio': 50, 'stock': 4},
        {'nombre': 'C', 'precio': 80, 'stock': 2},
    ]

    resultado = filtrar_y_ordenar_productos(productos_ejemplo)
    
    print("Resultado de la prueba:")
    for producto in resultado:
        print(f"{producto['nombre']} ({producto['precio']})")
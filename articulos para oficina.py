# Inicializar variables
productos = {1: {'tipo': 'A', 'precio': 0, 'cantidad': 0},
             2: {'tipo': 'B', 'precio': 0, 'cantidad': 0},
             3: {'tipo': 'C', 'precio': 0, 'cantidad': 0}}
totales_por_tipo = {'A': 0, 'B': 0, 'C': 0}
cantidades_por_tipo = {'A': 0, 'B': 0, 'C': 0}

# Función para calcular aumento de precio
def calcular_aumento_precio(precio, promedio):
    if precio > promedio + 400:
        nuevo_precio = precio * 1.07
        return nuevo_precio
    else:
        return precio

# Entrada de datos
while True:
    codigo = int(input("Ingrese código de artículo (-1 para finalizar): "))
    if codigo == -1:
        break
    
    cantidad = int(input("Ingrese cantidad vendida: "))
    precio = float(input("Ingrese precio unitario: "))

    # Actualizar totales
    tipo = productos[codigo]['tipo']
    totales_por_tipo[tipo] += cantidad * precio
    cantidades_por_tipo[tipo] += cantidad
    productos[codigo]['precio'] = precio
    productos[codigo]['cantidad'] += cantidad

# Calcular tipo de producto más vendido
tipo_mas_vendido = max(totales_por_tipo, key=totales_por_tipo.get)

# Calcular importe promedio por artículo
promedio_por_articulo = {codigo: productos[codigo]['precio'] * productos[codigo]['cantidad'] / cantidades_por_tipo[productos[codigo]['tipo']]
                         for codigo in productos}

# Calcular aumento de precio y mostrar información
print("Tipo de producto más vendido:", tipo_mas_vendido)
print("Importe total vendido por cada tipo de artículo:")
for tipo, total in totales_por_tipo.items():
    print(f"Tipo {tipo}: ${total:.2f}")
print("Importe promedio de venta por cada artículo:")
for codigo, promedio in promedio_por_articulo.items():
    print(f"Código {codigo}: ${promedio:.2f}")
    nuevo_precio = calcular_aumento_precio(productos[codigo]['precio'], promedio)
    if nuevo_precio:
        print(f"Nuevo precio para código {codigo}: ${nuevo_precio:.2f}")

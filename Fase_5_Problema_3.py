# Yobany Ramírez Moreno : 213022_866
#Problema 3 Inventaruio de un almacén


# Creamos la Matriz

inventario = [
    [1052, "Jabón de Mascota Barra", 25,100],
    [5841, "Comida para Gato x Kilo", 50, 200],
    [7845, "Cama para perro pequeña", 25, 20],
    [5842, "Comoda para Perro Bulto", 40, 30],
    [1061,"Shampoo para Mascota 500ml", 15, 150],
]

# creamos la función para controlar el inventario

def control_inventario(stock_actual, stok_mínimo):
    if stock_actual < stok_mínimo:
        cantidad=stok_mínimo - stock_actual
        return cantidad
    else:
        return 0

# Imprimimos el informe

print("="*50)
print("LA CASA DE LA MASCOTA -INFORME DE INVENTARIO")
print("="*50)
print()

for producto in inventario:
    codigo = producto[0]
    nombre = producto[1]
    stock_actual = producto[2]
    stock_minimo = producto[3]

    cantidad_a_pedir = control_inventario (stock_actual, stock_minimo)
    if cantidad_a_pedir > 0:
        print(f"Código: {codigo} -  Producto: {nombre} ")
        print(f"Stock Actual: {stock_actual}")
        print(f"Stock Mínimo: {stock_minimo}")
        print(f"Cantidad a Pedir: {cantidad_a_pedir}")
        print("-"*50)   
    else:
        print(f"Producto: {nombre} | Código: {codigo} | Stock suficiente (no pedir)")

print()
print("="*50)
print("Una vez vinalizado el informe, enviarlo a almacén con copia a contabilidad")
print("Cordialmente, Departamento de Compras")


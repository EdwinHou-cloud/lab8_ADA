import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo con categorías
productos = ['Arroz', 'Azúcar', 'Cereal', 'Harina', 'Leche', 'Manzanas', 'Naranjas', 'Pan', 'Peras', 'Plátanos', 'Tomate']
precios = [3.50, 2.00, 4.25, 1.75, 2.50, 3.00, 4.00, 1.50, 2.75, 2.80, 3.20]
categorias = ['Granos', 'Granos', 'Cereales', 'Granos', 'Lácteos', 'Frutas', 'Frutas', 'Panadería', 'Frutas', 'Frutas', 'Verduras']

# Crear un DataFrame
data = {'Producto': productos, 'Precio': precios, 'Categoría': categorias}
df = pd.DataFrame(data)

# Mostramos la tabla de productos y precios
print("Datos de Productos y Precios:")
print(df)

# Agrupamos por categoría y sumamos los precios
df_categoria = df.groupby('Categoría').sum()

# Graficamos una gráfica de pastel de precios por categoría
plt.figure(figsize=(8, 8))
plt.pie(df_categoria['Precio'], labels=df_categoria.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Precios por Categoría de Producto')
plt.show()

# Función de búsqueda binaria para productos
def busqueda_binaria_producto(lista, objetivo):
    lista_ordenada = sorted(lista)
    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista_ordenada[medio] == objetivo:
            return medio  # Se encontró el producto
        elif lista_ordenada[medio] < objetivo:
            inicio = medio + 1  # Busca en la mitad derecha
        else:
            fin = medio - 1  # Busca en la mitad izquierda
    
    return -1  # No se encontró el producto

# Función de búsqueda binaria para precios
def busqueda_binaria_precio(lista_precios, objetivo):
    lista_precios_ordenada = sorted(lista_precios)
    inicio = 0
    fin = len(lista_precios_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista_precios_ordenada[medio] == objetivo:
            return medio  # Se encontró el precio
        elif lista_precios_ordenada[medio] < objetivo:
            inicio = medio + 1  # Busca en la mitad derecha
        else:
            fin = medio - 1  # Busca en la mitad izquierda
    
    return -1  # No se encontró el precio

# Buscar un producto
producto_a_buscar = 'Leche'
indice_producto = busqueda_binaria_producto(productos, producto_a_buscar)

if indice_producto != -1:
    print(f"Producto '{producto_a_buscar}' encontrado en el índice: {indice_producto}")
else:
    print(f"Producto '{producto_a_buscar}' no encontrado.")

# Buscar un precio
precio_a_buscar = 2.50
indice_precio = busqueda_binaria_precio(precios, precio_a_buscar)

if indice_precio != -1:
    print(f"Precio {precio_a_buscar} encontrado en el índice: {indice_precio}")
else:
    print(f"Precio {precio_a_buscar} no encontrado.")

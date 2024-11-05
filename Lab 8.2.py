import matplotlib.pyplot as plt
import pandas as pd

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # Se encontró el producto
        elif lista[medio] < objetivo:
            inicio = medio + 1  # Busca en la mitad derecha
        else:
            fin = medio - 1  # Busca en la mitad izquierda
    
    return -1  # No se encontró el producto

# Datos de ejemplo
productos = ['Arroz', 'Azúcar', 'Cereal', 'Harina', 'Leche', 'Manzanas', 'Naranjas', 'Pan', 'Peras', 'Plátanos', 'Tomate']
precios = [3.50, 2.00, 4.25, 1.75, 2.50, 3.00, 4.00, 1.50, 2.75, 2.80, 3.20]

# Creamos un DataFrame para mostrar los datos originales
data = {'Producto': productos, 'Precio': precios}
df = pd.DataFrame(data)

# Mostramos la tabla
print(df)

# Graficamos los datos originales
plt.figure(figsize=(10, 6))
plt.bar(df['Producto'], df['Precio'], color='blue')
plt.title('Precios de Productos')
plt.xlabel('Producto')
plt.ylabel('Precio')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Mostrar gráfico
plt.tight_layout()
plt.show()

# Buscar un producto
producto_a_buscar = 'Leche'
indice = busqueda_binaria(sorted(productos), producto_a_buscar)

if indice != -1:
    print(f"Producto '{producto_a_buscar}' encontrado en el índice: {indice}")
else:
    print(f"Producto '{producto_a_buscar}' no encontrado.")
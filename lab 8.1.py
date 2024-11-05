import matplotlib.pyplot as plt
import pandas as pd

# Función del algoritmo burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Datos de ejemplo
productos = ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 'Kiwi']
precios = [3.50, 2.00, 4.25, 1.75, 2.50]

# Usamos el algoritmo burbuja para ordenar precios y productos
precios_ordenados = bubble_sort(precios.copy())
productos_ordenados = [producto for _, producto in sorted(zip(precios, productos))]

# Creamos un DataFrame para mostrar los datos
data = {'Producto': productos_ordenados, 'Precio': precios_ordenados}
df = pd.DataFrame(data)

# Mostramos la tabla
print(df)

# Graficamos los datos
plt.figure(figsize=(8, 5))
plt.bar(df['Producto'], df['Precio'], color='blue')
plt.title('Precios de Productos Ordenados')
plt.xlabel('Producto')
plt.ylabel('Precio')
plt.grid(axis='y')

# Mostrar gráfico
plt.show()
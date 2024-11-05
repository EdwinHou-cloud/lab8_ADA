import matplotlib.pyplot as plt
import pandas as pd

# Función del algoritmo burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Datos de ejemplo
productos = ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 'Kiwi']
precios = [3.50, 2.00, 4.25, 1.75, 2.50]

# Ordenamos precios y productos usando el algoritmo de burbuja
precios_ordenados = bubble_sort(precios.copy())
productos_ordenados = [producto for _, producto in sorted(zip(precios, productos))]

# Creamos un DataFrame para mostrar los datos
data = {'Producto': productos_ordenados, 'Precio': precios_ordenados}
df = pd.DataFrame(data)

# Mostrar la tabla
print(df)

# Configuramos el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(df['Producto'], df['Precio'], marker='o', color='purple', linestyle='-', linewidth=2, markersize=8)
plt.title('Precios de Productos Ordenados', fontsize=16)
plt.xlabel('Producto', fontsize=14)
plt.ylabel('Precio', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# Agregamos etiquetas de los valores
for i, precio in enumerate(df['Precio']):
    plt.text(i, precio + 0.1, f"${precio:.2f}", ha='center', fontsize=12, color='darkred')

# Mostrar gráfico
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo con categorías
productos = ['Arroz', 'Azúcar', 'Cereal', 'Harina', 'Leche', 'Manzanas', 'Naranjas', 'Pan', 'Peras', 'Plátanos', 'Tomate']
precios = [3.50, 2.00, 4.25, 1.75, 2.50, 3.00, 4.00, 1.50, 2.75, 2.80, 3.20]
categorias = ['Granos', 'Granos', 'Cereales', 'Granos', 'Lácteos', 'Frutas', 'Frutas', 'Panadería', 'Frutas', 'Frutas', 'Verduras']

# Crear un DataFrame
data = {'Producto': productos, 'Precio': precios, 'Categoría': categorias}
df = pd.DataFrame(data)

# Agrupamos por categoría y sumamos los precios
df_categoria = df.groupby('Categoría').sum()

# Graficamos una gráfica de pastel de precios por categoría
plt.figure(figsize=(8, 8))
plt.pie(df_categoria['Precio'], labels=df_categoria.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Precios por Categoría de Producto')
plt.show()

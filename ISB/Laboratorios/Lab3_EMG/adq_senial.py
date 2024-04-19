import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

fs= 1000;

# Ruta al archivo de texto
archivo = 'Kim.txt'

# Leer el archivo omitiendo las líneas de comentarios y el encabezado
data = pd.read_csv(archivo, delimiter='\t', comment='#', header=None)

# Extraer la sexta columna, que corresponde al índice 5 (los índices empiezan en 0)
amplitud = data.iloc[:, 5]

# Convertir los datos de la sexta columna a una lista de Python

# Convertir valores crudos a milivoltios
voltaje_por_unidad = 3.3 / 1023
valores_milivoltios = amplitud * voltaje_por_unidad * 1000  # Conversión a mV

# Crear una lista para el eje X, que va desde 1 hasta el número de elementos en valores_y
n = np.arange(1, len(valores_milivoltios) + 1)
ts=n/fs;

# Crear un plot usando matplotlib
plt.figure(figsize=(10, 5))  # Ajustar tamaño de la figura
plt.plot(ts, valores_milivoltios, linestyle='-', color='b')  # Línea azul con marcadores en forma de círculo
plt.title('Tiempo vs mV')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.grid(True)  # Añadir una cuadrícula para mejor visualización
plt.show()

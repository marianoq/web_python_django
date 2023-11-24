import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener la ruta del script actual
current_path = os.path.dirname(os.path.abspath(__file__))

# Crear la carpeta "mapa_html" si no existe
folder_path = os.path.join(current_path, 'datasets')
os.makedirs(folder_path, exist_ok=True)

# Ruta del archivo HTML en la carpeta "mapa_html"
file_read = os.path.join(folder_path, 'global_airports.csv')

data = pd.read_csv(file_read)

plt.scatter(data.longitude,data.latitude)
plt.show()
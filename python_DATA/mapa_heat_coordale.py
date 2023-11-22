from folium.plugins import HeatMap #importar modulo
import folium
import webbrowser
import numpy as np
import random
import matplotlib.pyplot as plt
import os

# Obtener la ruta del script actual
current_path = os.path.dirname(os.path.abspath(__file__))


#generar datos aleatorios de ubicacion
data=[[random.uniform(4.56,4.57),random.uniform(-74.154,-74.141)] for i in range(50) ]
data_array=np.array(data) #transformar lista en un array
#buscar el punto medio para graficar el mapa de fondo
xm=data_array[:,0].mean() #calcular la media de latitud
ym=data_array[:,1].mean() #calcular la media de longitud
plt.scatter(data_array[:,0], data_array[:,1])
plt.show()

#crear mapa
mapa = folium.Map([xm,ym], tiles="OpenStreetMap", zoom_start=16)

#dibujar mapa de color
HeatMap(data).add_to(mapa)

# Crear la carpeta "mapa_html" si no existe
folder_path = os.path.join(current_path, 'mapa_html')
os.makedirs(folder_path, exist_ok=True)

# Ruta del archivo HTML en la carpeta "mapa_html"
map_file_path = os.path.join(folder_path, 'Heat.html')

#guardar mapa
mapa.save(map_file_path)

#mostrar mapa
webbrowser.open(map_file_path)
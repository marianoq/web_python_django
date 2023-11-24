import pandas as pd
import os

# Obtener la ruta del script actual
current_path = os.path.dirname(os.path.abspath(__file__))

# Crear la carpeta "mapa_html" si no existe
folder_path = os.path.join(current_path, 'datasets')
os.makedirs(folder_path, exist_ok=True)

# Ruta del archivo HTML en la carpeta "mapa_html"
file_read = os.path.join(folder_path, 'ZoneA.dat')

data=pd.read_csv(file_read)

#extraer coordenadas
coordenadas=[] # definir una lista para guardar las coordenadas
#ciclo para OBTENER coordenadas
for d in range(9,len(data)):
    x=(data.iloc[d,0]).split(' ')[0];y=(data.iloc[d,0]).split(' ')[1]
    z=(data.iloc[d,0]).split(' ')[4]
    coordenadas.append([x,y,z])

for d in range(9,len(data)):
    x=float(data.iloc[d,0].split(' ')[0]);y=float(data.iloc[d,0].split(' ')[1])
    z=float(data.iloc[d,0].split(' ')[4]) #leer la permeabilidad en la posicion 4
    coordenadas.append([x,y,z])

#leer el fichero usando el modulo de geoestadistica
from geostatsmodels import utilities
#leer datos
file='ZoneA.dat'
z = utilities.readGeoEAS(path+file)
data = z[:,[0,1,2]]
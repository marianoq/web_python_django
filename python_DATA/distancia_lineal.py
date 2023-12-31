import PySimpleGUI as sg
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from folium import plugins
import webbrowser
import os

# Crear Objeto Nominatim
geolocator = Nominatim(user_agent="AppMap", timeout=10)

# Obtener la ruta del script actual
current_path = os.path.dirname(os.path.abspath(__file__))

# Definir el diseño de la interfaz
layout = [
    [sg.Text('Calculadora de Distancia', font=('Helvetica', 16))],
    [sg.Text('Origen:', size=(6, 1), font=('Helvetica', 12)), sg.InputText(size=(30, 1), font=('Helvetica', 12), key='origen')],
    [sg.Text('Destino:', size=(6, 1), font=('Helvetica', 12)), sg.InputText(size=(30, 1), font=('Helvetica', 12), key='destino')],
    [sg.Button('Calcular Distancia', size=(18, 1), font=('Helvetica', 12), key='Distancia', button_color=('white', '#007F00')),
     sg.Text(font=('Helvetica', 14)), sg.Text('', size=(20, 1), font=('Helvetica', 12), key='-OUTPUT-')],
    [sg.Button('Salir', size=(15, 1), font=('Helvetica', 12), key='Salir', button_color=('white', '#E53E3E')),
     sg.Button('Ver en el Mapa', size=(20, 1), font=('Helvetica', 12), key='Mapa', button_color=('white', '#004080'))],
]

# Crear la ventana
window = sg.Window('Generar Mapa y Distancia LINEAL', layout, finalize=True, auto_size_buttons=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Salir':
        break

    if event == 'Distancia':
        try:
            origen = geolocator.geocode(values['origen'])
            destino = geolocator.geocode(values['destino'])

            if origen is None or destino is None:
                raise ValueError("Ubicación no encontrada para uno de los lugares ingresados.")

            if None in (origen.latitude, origen.longitude, destino.latitude, destino.longitude):
                raise ValueError("Ubicación no válida para uno de los lugares ingresados.")

            dist = geodesic((origen.latitude, origen.longitude), (destino.latitude, destino.longitude)).kilometers
            window['-OUTPUT-'].update(f'Distancia: {dist:.2f} km')

        except Exception as e:
            window['-OUTPUT-'].update(f'Error: {str(e)}')

    if event == 'Mapa':
        try:
            # Crear la carpeta "mapa_html" si no existe
            folder_path = os.path.join(current_path, 'mapa_html')
            os.makedirs(folder_path, exist_ok=True)

            # Ruta del archivo HTML en la carpeta "mapa_html"
            map_file_path = os.path.join(folder_path, 'mapa_distancia.html')

            coord = [[origen.latitude, origen.longitude], [destino.latitude, destino.longitude]]
            lat_prom = (origen.latitude + destino.latitude) / 2
            long_prom = (origen.longitude + destino.longitude) / 2

            minimap = plugins.MiniMap()
            mapa = folium.Map(location=[lat_prom, long_prom], tiles='OpenStreetMap')
            my_PolyLine = folium.PolyLine(locations=coord, weight=5)
            mapa.add_child(my_PolyLine)
            mapa.add_child(minimap)

            # Guardar el mapa en la carpeta "mapa_html"
            mapa.save(map_file_path)

            # Abrir el mapa desde la carpeta "mapa_html"
            webbrowser.open(map_file_path)

        except Exception as excep:
            window['-OUTPUT-'].update(f'Error: {str(excep)}')

window.close()

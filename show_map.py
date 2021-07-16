import folium
from pymongo import MongoClient

client = MongoClient('localhost')

fusadb = client['fusadb']

col1 = fusadb['Archivos']

mapa = folium.Map(location =[-39.823641, -73.226158], zoom_start = 14)

for doc in col1.find():
    latitud = doc['latitud']
    longitud = doc['longitud']
    fecha = doc['fecha_de_grabacion']
    tooltip = doc['fecha_de_grabacion']
    folium.Marker([latitud,longitud], popup = fecha, tooltip = tooltip).add_to(mapa)

mapa.save('C:\\Users\\Giorgio\\Desktop\\Prueba2_BD\\prueba.html')

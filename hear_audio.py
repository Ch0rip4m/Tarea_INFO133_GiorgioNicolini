from pymongo import MongoClient
from tkinter import *
from playsound import playsound 

client = MongoClient('localhost')

fusadb = client['fusadb']

col2 = fusadb['Audios']

seguir = True 

while(seguir):

    print("Seleccion de audio")
    fecha = input("Para buscar su archivo de audio ingrese la fecha (DD/MM/AA): ")

    for documento in col2.find():
        if(documento['fecha_audio'] == fecha):
            nombreAudio = documento['nombre_archivo']

    nombreAudio = "salida" + nombreAudio
    data = col2.find_one({'fecha_audio': fecha})
        
    with open(nombreAudio, "wb") as f:
        f.write(data['file'])

    print("Reproduciendo audio solicitado")
    
    playsound(nombreAudio)

    pregunta = input("Desea escuchar otro audio? (S/N): ")

    if(pregunta == "N"):
        seguir = False



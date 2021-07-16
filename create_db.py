from pymongo import MongoClient

client = MongoClient('localhost')

fusadb = client['fusadb']

col1 = fusadb['Archivos']


col1.insert_many([{
    'ID_Archivo' : '1',
    'fecha_de_grabacion' : '11/07/21',
    'ciudad' : 'Valdivia',
    'duracion' : '1:00',
    'formato' : 'wav',
    'latitud' : '-39.842679',
    'longitud' : '-73.243428',
    'exterior' : True, 
    'usuario' : { 'RUT' : '19814279-4' , 'nombre' : 'Giorgio' , 'apellido' : 'Nicolini' },
    'segmentos' : {
        'ID_segmento' : '1',
        'formato' : 'wav' , 
        'duracion' : '0:05', 
        'inicio' : '0:55', 
        'fin' : '1:00',
        'etiquetas' : { 'nombre_fuente' : 'Animal' , 'descripcion' : 'grabacion de un perro en el sector el Bosque' , 'id_analizador' : '1'}}
    },
    {'ID_Archivo' : '2',
    'fecha_de_grabacion' : '12/07/21',
    'ciudad' : 'Valdivia',
    'duracion' : '0:30',
    'formato' : 'wav',
    'latitud' : '-39.812753',
    'longitud' : '-73.243734',
    'exterior' : False, 
    'usuario' : { 'RUT' : '10644243-6' , 'nombre' : 'Jorge' , 'apellido' : 'Nicolini' },
    'segmentos' : {
        'ID_segmento' : '2',
        'formato' : 'wav' , 
        'duracion' : '0:05', 
        'inicio' : '0:00', 
        'fin' : '0:05',
        'etiquetas' : { 'nombre_fuente' : 'Vehiculo' , 'descripcion' : 'grabacion de un policia en el sector de isla teja' , 'id_analizador' : '1'}}
     },
    {'ID_Archivo' : '3',
    'fecha_de_grabacion' : '02/07/21',
    'ciudad' : 'Valdivia',
    'duracion' : '0:32',
    'formato' : 'wav',
    'latitud' : '-39.808778',
    'longitud' : '-73.256980',
    'exterior' : True, 
    'usuario' : { 'RUT' : '10771670-k' , 'nombre' : 'Ivonne' , 'apellido' : 'Aguayo' },
    'segmentos' : {
        'ID_segmento' : '3',
        'formato' : 'wav' , 
        'duracion' : '0:05', 
        'inicio' : '0:12', 
        'fin' : '0:17',
        'etiquetas' : { 'nombre_fuente' : 'Mecanico' , 'descripcion' : 'grabacion de explocion en en sector centro' , 'id_analizador' : '2'}}
        }])

print('Datos importados a la base de datos fusadb en la coleccion Archivos')






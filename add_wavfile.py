from pymongo import MongoClient
from bson.binary import Binary
from bson import ObjectId
import pymongo, gridfs
from gridfs import GridFS
from pymongo import MongoClient

client = MongoClient('localhost')

fusadb = client['fusadb']

col2 = fusadb['Audios']

audioExplo = 'explosion.wav'

with open(audioExplo, "rb") as f:
    encoded = Binary(f.read())
col2.insert_one({'nombre_archivo': audioExplo, 'file': encoded, 'descripcion': 'grabacion de explocion en en sector centro','fecha_audio' : '02/07/21'  })

audioPerro = 'perro.wav'

with open(audioPerro, "rb") as f:
    encoded = Binary(f.read())
col2.insert_one({'nombre_archivo': audioPerro, 'file': encoded, 'descripcion' : 'grabacion de un perro en el sector el Bosque' , 'fecha_audio' : '11/07/21' })

audiopolicia = 'SirenadePolicia.wav'

with open(audiopolicia, "rb") as f:
    encoded = Binary(f.read())
col2.insert_one({'nombre_archivo': audiopolicia, 'file': encoded, 'descripcion': 'grabacion de un policia en el sector de isla teja', 'fecha_audio' : '12/07/21' })

print('Audios ingresados a la base de datos fusadb en la colecion Audios')

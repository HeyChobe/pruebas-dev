from pymongo import MongoClient

'''
# Al necesitar autentificación en un servidor

MongoClient('localhost', 
            port=27017, 
            username='user',
            password='pass')
'''

# Al tener un servidor local
conexion = MongoClient('localhost')

# Creando una BD
nueva_bd = conexion['alumnos']

# Creando una colección
coleccion = nueva_bd['PrimerCiclo']

# Insertando un documento
# coleccion.insert_one({
#     'nombre':'Carlos Cortez',
#     'edad': 20,
#     'apodo': 'Chobe'
# })

# Insertando varios documentos
# coleccion.insert_many([
#     {
#         'nombre':'Adriana Guardado',
#         'edad': 19,
#         'apodo': 'Egna'
#     },
#     {
#         'nombre':'Samantha Cortez',
#         'edad': 22,
#         'apodo': 'Sam'
#     },
# ])

# Una forma de mostrar
# for documento in coleccion.find({}):
#     print(documento)

documento = coleccion.find_one({
    "nombre":"Carlos Cortez"
})

print(documento)

coleccion.delete_one({
    "nombre":"Carlos Cortez"
})

coleccion.update_one(
    {
        "nombre":"Samantha Cortez"
    },
    {
        "$set": {
            "nombre":"Samy Cortez"
            }
    }
)

for documento in coleccion.find({}):
    print(documento)

# Equivalente a show.dbs
# print(conexion.list_database_names())
# print(nueva_bd.list_collection_names())
# print(coleccion.count_documents({}))

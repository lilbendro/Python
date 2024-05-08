#################################################
#             Trabajando con Mongo              #
#################################################

from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import sys, json


####################################
# Conectar con un servidor MONGODB #
####################################

#Creamos un objeto que almacenamos en la Variable ClientDB
#El objeto representa el cliente para trabajar con la base de datos de MongoDB
#Requiere una cadena de conexión
clientDB = MongoClient("mongodb://localhost:27017/") #IP:Puerto | A través del clinete accedemos a la base de datos

#Nos posicionamos sobre una base de datos, en el ejemplo sobre la base de datos ADMIN
db = clientDB.admin #Obtenemos la base de datos de ADMIN como "db"

#Enjucatamos un comando utilizando la función COMMAND
#El comando serverStatus nos retorna el estado del servidor en formato JSON
result = db.command("serverStatus")

print(result)


################################################
# Trabajar con base de datos y sus colecciones #
################################################
clientDB = MongoClient("mongodb://localhost:27017/")

# Mostrar el nombre de las bases de datos
print(clientDB.list_database_names())

for db in clientDB.list_database_names():
    print(f"Nombre: {db}")
    print(f" -> {clientDB[db].list_collection_names()}")

#Seleccionar una base de datos con la que vamos a trabajar
db = clientDB.northwind          #Sintaxis de objeto
db2 = clientDB["northwind"]      #Sintaxis de colección

#Mostrar las colecciones que tiene una base de datos
#Colecciones son equivalentes a tablas de Base de Datos Relacionales

print(db.list_collection_names())
print(db2.list_collection_names())

#Seleccionamos una colección con la que vamos a trabajar
collection = clientDB.northwind.customers
collection = clientDB["northwind"]["customers"]
collection = db.customers #Utilizando la variable que creamos antes
collection = db["customers"]

#Mostramos el número de documentos en la coleción
#Los documentos son equivalentes a los registros en bases de datos relacionales 
print (f"{collection.estimated_document_count()} documentos en {collection.name}")


################################################
#             Trabajar con documentos          #
################################################

#Mostrar el documento por el identificador del objeto
#Filtro: _id = identificador
result = collection.find_one({"_id": ObjectId("663a105ea40f52cc2d357da6")})
pprint(result)
print("")

# Mostrar el primer documento que coincide 
#Filtro: Country = USA
result = collection.find_one({"Country": "USA"}) #Le pasamos el filtro construido en formato JSON
pprint(result) #PPrint va saltando líneas para facilitar la lectura
print("")

#Mostrar todos los documentos que coinciden con el filtro
#Filtro: Country = USA
cursor = collection.find({"Country": "USA"}) #Usamos FIND esta vez, que arrojará un CURSOR
#Un cursor es similar al generador con funcionalidades extra
#pprint(f"Resultado de la búsqueda {cursor.count()} documentos.") #No disponible count() desde la versión 6
pprint(f"Resultado de la búsqueda {collection.count_documents({"Country": "USA"})} documentos.")

#Cuando ALIVE retorna TRUE significa que tenemos documentos pendientes de leer en el cursor
print(f"Documentos pendientes de leer: {cursor.alive}")
print("")

#Utilizamos WHILE para mostrar los documentos del cursor
#Bloque WHILE se ejecuta mientras ALIVE retorne TRUE (documentos pendientes de leer)
#Con la función .NEXT()

while cursor.alive == True: #Si es TRUE se puede simplificar en while cursor.alive
    document = cursor.next() #Con next según se lee el cursor se va borrando
    pprint(document)
    print("")
print(f"Documentos pendientes de leer: {cursor.alive}")


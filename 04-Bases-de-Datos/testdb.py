from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

clientDB = MongoClient("mongodb://localhost:27017/")
db = clientDB.northwind          
collection = db.customers 



#####################################################
# Ejemplos de búsquedas y utilización de operadores #
#####################################################

"""
===================================================

 Listado de operadores relacionales

===================================================

$eq - equal - igual
$lt - low than - menor que
$lte - low than equal - menor o igual que
$gt - greater than - mayor que
$gte - greater than equal - mayor o igual que
$ne - not equal - distinto
$in - in - dentro de
$nin - not in - no dentro de
$regex - cumple con la expresión regular
"""

cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": "USA"}).limit(3) #Se queda con los 3 primeros
cursor = collection.find({"Country": "USA"}).skip(5) #Se salta los tres primeros
cursor = collection.find({"Country": "USA"}).sort("City") #Ordena por "city"
cursor = collection.find({"Country": "USA"}).sort({"City": -1}) #Ordenación descendente


#Buscar clientes de USA, ejemplos con y sin operador
cursor = collection.find({"Country": "USA"}) #Sin operador
cursor = collection.find({"Country":{"$eq": "USA"}}) #Con operador $eq

#Buscar clientes de USA y México, ordenados por país y ciudad
cursor = collection.find({"Country": {"$in": ["USA", "Mexico"]}}).sort([("Country", 1), ("City", 1)]) #Le pasamos una lista al operador

#Buscar clientes que contienen DE en la clave CustomerID
cursor = collection.find({"CustomerID": {"$regex": "DE"}})

#Buscar clientes que el CustomerID comienza por A y finaliza con 4 caracteres más
cursor = collection.find({"CustomerID": {"$regex": "A[A-Z]{4}"}})

#Buscar clientes de la ciudad de San Francisco en USA
cursor = collection.find({"Country": "USA", "City": "San Francisco"}) #Operador AND implícito

#Buscar clientes de la ciudad de San Francisco en USA con el operador AND
cursor = collection.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]}) #Pasamos los dos campos en una colección

#Buscar clientes de GERMANY o USA utilizar el operador OR
cursor = collection.find({"$or": [{"Country": "USA"}, {"Country": "Germany"}]})

#Buscar los clientes de México y sus pedidos
cursor = collection.find({"Country": "Mexico"})



while cursor.alive == True: #Si es TRUE se puede simplificar en while cursor.alive
    document = cursor.next() #Con next según se lee el cursor se va borrando
    print(f"{document["CustomerID"]} - {document["CompanyName"]} - {document["Country"]} - {document["City"]}")
    
    pedidos = clientDB.northwind.orders.find({"CustomerID": document["CustomerID"]})
    while(pedidos.alive):
        pedido = pedidos.next()
        print(f">>> {pedido["OrderID"]} {pedido["OrderDate"]}")

print("")


#Buscar los clientes de Mexico y sus pedidos utilizando la función AGGREGATE
cursor = db.customers.aggregate([
    {"$match": {"Country": "Mexico"}},
    {"$sort": {"City": 1}},
    {"$lookup": {
        "from": "orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Pedidos"
    }}
])

#LOOKUP nos permite hacer subconsultas en otras colecciones

while (cursor.alive == True):
    document = cursor.next()
    print(f"{document["CustomerID"]}# {document["CompanyName"]} - {document["City"]} ({document["Country"]})")
    
    for pedido in document["Pedidos"]:
        print(f" >> {pedido["OrderID"]}# - {pedido["OrderDate"]}")
    
print("")
#################################################
#                     JSON                      #
#         (JavaScript Object Notation)          #
#################################################

#La seriealización convierte objetos en bytes

import json

frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"] #colección alfanumérica

#Conversión de objetos en JSON con dumps
frutasJSON = json.dumps(frutas) #Convertiremos un objeto lista en una texto plano

#Comprobaciones
print(f"Lista: {frutas}")
print(f"Posición 2: {frutas[2]}") #Nos arroja la segunda fruta, "pomelo"
print(f"{type(frutas)}") #Nos dirá que es una LIST

print(f"Json: {frutasJSON}")
print(f"Posición 2: {frutasJSON[2]}") #Nos arroja el carácter en la posición 2ª, "n"
print(f"{type(frutasJSON)}") #Nos dirá que es un STRING, un texto 
print("")

#Conversión de JSON en objetos
frutas2 = json.loads(frutasJSON)
print(f"Lista: {frutas2}")
print(f"Posición 2: {frutas2[2]}") #Nos arroja la segunda fruta
print(f"{type(frutas2)}") #Nos dirá que es una lista
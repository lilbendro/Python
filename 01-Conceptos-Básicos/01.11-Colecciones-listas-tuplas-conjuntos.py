#################################################
#                   Colecciones                 #
#            Listas, tuplas,conjuntos           #
#################################################


#Encerrado los valores con [] tenemos una lista 
lista = ["naranja", "limón", "pomelo", "lima", "mandarina"]
#Si sustituimos los [] por () tendremos una Tupla, cuyos valores no se pueden modificar, borrar o añadir
tupla = ("naranja", "limón", "pomelo", "lima", "mandarina")
#Lo mismo con {} sería un Conjunto, cuyos valores estarán desordenados (sin posición)
Conjunto = {"naranja", "limón", "pomelo", "lima", "mandarina"}


#Declaración de variables 
vacia = []
frutas = ["naranja", "limón", "pomelo", "líma", "mandarina"] 

print(frutas) #Pintar la cadena
print(frutas[2])  #Pintar posición 2
print(len(frutas)) #Longitud de la cadea
print(f"Naranja se repite {frutas.count("naranja")} veces")

#Modificamos el valor de una posición
frutas[2] = "fresa"
print(f"Posición 2: {frutas[2]}")

#Añadir un valor a la lista con APPEND, yéndose al final
frutas.append("manzana")
frutas.append("melón")
print(f"Contenido de frutas {frutas}") 

#Añadir un nuevo valor en una posición utilizando INSERT (index, value) desplazando a los demás
frutas.insert(1, "sandia")
print(f"Contenido de frutas {frutas}") 

#Añadir varios elementos utilizando EXTEND(list)
nuevasFrutas = ["maracuya", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas) # También es válido lista1 += lista2 
print(f"Contenido de frutas {frutas}") 

frutas.extend(["platano", "pera"])
print(f"Contenido de frutas {frutas}") 

#Añadir un elemento si no existe
print(f"melocotón existe en frutas: {("melocotón" in frutas)}")
print(f"melocotón no existe en frutas: {("melocotón" not in frutas)}")

if ("melocotón" not in frutas):
    frutas.append("melocotón")

print(f"Contenido de frutas {frutas}") 

#Eliminar un elemento indicando su posición (mandarina)
frutas.pop(5)
print(f"Contenido de frutas {frutas}") 

#Eliminar un elemento indicando su nombre
frutas.remove("naranja") #Sólo eliminará el primer elemento, si se repité habrá que ejecutarlo varias veces
print(f"Contenido de frutas {frutas}")

#Para evitar errores podemos preguntar por la existencia de un valor antes de eliminar
if ("uva" in frutas):
    frutas.remove("uva")
                  
#Inertir el orden de los valores con REVERSE
frutas.reverse()
print(f"Contenido de frutas {frutas}")

#Ordenador los elementos de la lista por orden alfabético
frutas.sort()
print(f"Contenido de frutas {frutas}")

frutas.sort(reverse=True)
print(f"Contenido de frutas {frutas}")

#Recorrer la lista y mostramos sus valores
for fruta in frutas:
    print(f"{fruta}")

for index in range(len(frutas)):
    print(f"{index}# {frutas[index]}")

for index, value in enumerate(frutas):
    print(f"{index}# {value}")
print("")

#Copiar una lista
vacia = frutas.copy()
print(f"Contenido de vacía {vacia}")

#Eliminar todos los elementos de una lista
frutas.clear()
print(f"Contenido de frutas {frutas}")


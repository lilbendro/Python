#################################################
#                   Colecciones                 #
#                  Diccionarios                 #
#################################################

#Un diccionario se construye con {} y a cada valor le acompaña una clave alfanumérica que sirve para indexarlo
vacio = {}
frutas = {"NA":"naranja", "LI":"limón","PO":"pomelo", "LM":"lima", "MA":"mandarina"}

print(f"Contenido de frutas {frutas}")

#Mostrar el valor de un elemento con la clave ( PO = pomelo)
print(f"Clave de PO: {frutas["PO"]}") 

#Mostrar el valor de unelemento con la función get
print(f"Clave PO: {frutas.get("PO")}")
print(f"Clave ML: {frutas.get("ML")}") #El método GET permite llamar a elementos que no existen devolviendo NONE, sin provocar un error

#Mostrar el número de elementos que contiene el diccionario
print(f"Número de elementos {len(frutas)}")

#Mostrar las claves del diccionario
print(f"Claves: {list(frutas.keys())}")

#Modificar valores del diccionario
frutas["NA"] = "sandia"
print(f"Contenido de NA {frutas["NA"]}")
frutas.update({"NA":"ciruela"})
print(f"Contenido de NA {frutas["NA"]}")

#Añadir nuevos valores al diccionario
frutas["ML"] = "melón" #si no existe dicha clave se crea, sino se sobreescribe 
frutas.update({"MZ" : "manzana"})
print(f"Contenido de Frutas {frutas}")

#Eliminar valores
frutas.pop("NA")
del frutas["MZ"]
print(f"Contenido de Frutas {frutas}")

#Recorremos el diccionario mostrando los valores
for key in frutas:
    print(f"{key}# {frutas[key]}")
    
#Copiar una diccionario
vacio = frutas.copy()
print(f"Contenido de vacía {vacio}")

#Eliminar todos los elementos de un diccionario
frutas.clear()
print(f"Contenido de frutas {frutas}")
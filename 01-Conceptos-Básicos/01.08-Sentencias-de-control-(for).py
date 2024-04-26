#################################################
#             Sentencias de control             #
#                       For                     #
#################################################

#Declaración de variables
citricos = ["naranja", "limón", "pomelo", "lima", "mandarina"]

#Utilizamos FOR para recorrer colecciones con IN
#No tenemos la posición de los elementos
print("\n============\n")

for fruta in citricos: #fruta es una variable, pasará recorriendo la colección guardando cada valor
    print(f"->{fruta}")

print("\n============\n")

#Utilizamos FOR para crear contadores con RANGE
#La combinación de RANGE con LEN nos permite recorrer colecciones
#Tenemos la posición de cada elemento en la colección

#contador de 0 a 10
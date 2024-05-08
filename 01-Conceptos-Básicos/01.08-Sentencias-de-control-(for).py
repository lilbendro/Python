#################################################
#             Sentencias de control             #
#                       For                     #
#################################################

#Declaración de variables
citricos = ["naranja", "limón", "pomelo", "lima", "mandarina"] #Los corchetes crean una colección, si fueran paréntesis sería una tupla

#Utilizamos FOR para recorrer colecciones con IN
#No tenemos la posición de los elementos
print("\n============\n")

for fruta in citricos: #fruta es una variable, pasará recorriendo la colección guardando cada valor
    print(f"->{fruta}")

#El uso de ENUMERATE nos permite recorrer colecciones conociento el índice y el valor
for index, fruta in enumerate(citricos):
    print(f"->{index}# {citricos[index]}")

print("\n============\n")

#Utilización de CONTINUE y BREAK con las sentencias FOR
    #Break finaliza la ejecución del bloque de sentencias y el FOR
for fruta in citricos:
    if(fruta == "pomelo"): #Para cuando el for cuando lee pomelo
        break 
    print(f"->{fruta}")
    #Continue finaliza la ejecución del bloque de sentencias 
for fruta in citricos:
    if(fruta == "pomelo"): #se salta pomelo
        continue 
    print(f"->{fruta}")

#Utilizamos FOR para crear contadores con RANGE


#contador de 0 a 10
for numero in range(11):
    print(f"->{numero}")

print("\n============\n")

#contador de 10 a 20, de 2 en 2
for numero in range(10, 21, 2): #Valor inicio, valor final y valor de incremento
    print(f"->{numero}")

print("\n============\n")

#contador de 20 a 5, en -3
for numero in range(20, 4, -3):
    print(f"->{numero}")

print("\n============\n")

#La combinación de RANGE con LEN nos permite también recorrer colecciones
#Aquí si tenemos la posición de cada elemento
for index in range(len(citricos)): #Index es una variable, range(len(X)) nos da el valor de la posición
    print(f"->{index}# {citricos[index]}")



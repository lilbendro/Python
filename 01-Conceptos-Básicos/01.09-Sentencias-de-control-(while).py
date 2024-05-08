#################################################
#             Sentencias de control             #
#                     While                     #
#################################################

#Uso de While
print (f"inicio de while")

valor = 0

while (valor < 5):
    valor += 1
    if (valor == 3): 
        continue
    print(f"Valor actual {valor}")

print(f"Fin de While \n")

#Utilizamos el while para recorrer colecciones
index = 0
citricos = ["naranja", "limón", "pomelo", "lima", "mandarina"]

while(index<len(citricos)):
    print(f"-> {index}# {citricos[index]}")
    index += 1 
print("Fin del while cítrico \n")

#Implementar la funcionalidad que otros lenguajes ofrecen con DO/WHILE
# consiguiendo que el bloque de sentencias se ejecute al menos una vez
valor = 0

while(True): #True hace que siempre se cumpla condición del while
    valor += 1
    print(f"Valor actual es {valor}")

    if(valor > 4):
        break #Rompe el while 


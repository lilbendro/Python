#################################################
#            Declaración de variables           #
#################################################
#                                               #
#  Síntaxis: [nombre variable = valor inicial]  #
#                                               #
#  Ejemplos:                                    #
#    número = 20                                #
#    saludo = "Hola, mundo"                     #
#################################################

# Declaración de variables
numero = 10
Numero = 20
saludo = "Hola, Mundo."

# Mostrar el contenido de las variables
print(numero)
print(Numero) # Sensibilidad a las mayúsculas
print(saludo)

print(numero + Numero)
print(numero - 25)
print(saludo + " ¿Qué tal?") #Concatenación
print("Y ahora...\n¡pego un salto!") #Salto de linea

# Mostrar tipo de variables
print(type(saludo)) #String
print(type(numero)) #int
print(type(3)) #Int
print(type(3.1)) #Float
print(type("3.1")) #String
print(type(3==3)) #Bool
print(type(3!=3)) #Bool
print(type(('1', '2', '3'))) #Tuple
print(type(["1", "2", "3"])) #List
print(type({"1", "2", "3"})) #Set
print(type([1, 2, 3]))  #List


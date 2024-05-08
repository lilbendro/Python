#################################################
#                   Funciones                   #
#################################################
from datetime import datetime

#Ejemplo de función que no recibe datos (sin parámetros) y no retorna datos
def func1():
    """Parámetros vacíos y no retorna datos""" #Nuevo tipo de comentario, aparece si pones el puntero en func1()
    print(f"¿Qué dise el polla?")

#Ejemplo de función que recibe datos (con parámetros) y no retorna datos
def func2(nombre, numero):
    """Con parámetros y no retorna datos""" 
    print(f"Me llamo {nombre} y mi ID es {numero}")

#Ejemplo de función que recibe datos (con parámetros) y retorna datos
def func3(frase):
    """Con parámetros y retorna datos""" 
    cantidad = len(frase)
    return cantidad #Retorna datos, no significa ue automáticamente se pinte

#Ejemplo de función que no recibe datos (sin parámetros) y retorna datos
def func4():
    """Parámetros vacíos y retorna datos"""
    return datetime.now().date().strftime("%A") 

#Llamamos a las funciones
func1()
func2("Paco", 2) #Tenemos que pasarle valor a las variables de los parámetros
print(func3("Hay lmao")) #Retorna cantidad, así que hay que recogerla en una variable y luego pintarla, o pintar directamente el resultado
print(func4())

#################################

def Resta(a,b): #Todos los parámetros son obligatorios
    return a - b
print (f"1) 85 - 10 = {Resta(85,10)}") #Asignamos valor por posición
print (f"1) 85 - 10 = {Resta(b=85,a=10)}") #Asignamos valor por nombre

def Resta1(a,b=10): #Solo el parámetro A es obligatorio
    return a - b
print (f"2) 85 - 10 = {Resta1(85)}") #Solo damos el valor de A
print (f"2) 85 - 10 = {Resta1(b=100,a=10)}") #Asignamos valor por nombre, cambiando el de B

def Resta2(a=85,b=10): #Todos los parámetros son opcionales
    return a - b
print (f"3) 85 - 10 = {Resta2()}") #No indicamos parámetros
print (f"3) 85 - 10 = {Resta2(25)}") #Asignamos valor por posición, cambiándolo
print (f"3) 85 - 10 = {Resta2(b=15,a=10)}") #Asignamos valor por nombre, cambiándalo
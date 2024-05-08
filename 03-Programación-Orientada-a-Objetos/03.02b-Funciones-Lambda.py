#################################################
#              Funciones  Lambda                #
#################################################

from functools import reduce

numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]

#Funcion que retorne una lista con los números mayores de de 100
def MayorDeCien(lista):
    resultado = [] 

    for numero in numeros:
        if numero > 100:
            resultado.append(numero)
    return resultado
    
print(f"Función estandar {MayorDeCien(numeros)}")

#Función que return TRUE cuando un número es mayor de 100, si no retorna FALSE
def NumMayorCien(numero):
    if (numero > 100):
        return True
    else:
        return False
    #Filter aplica la función a una colección, quedándose a aquellos que devuelven TRUE
print(f"FILTER en función estandar {list(filter(NumMayorCien,numeros))}") #List convierte el objeto FILTER que devuelve ese mismo método

#Extraer numeros mayores de 100 con FILTER y una función LAMBDA
print(f"FILTER en función LAMBDA {list(filter(lambda numero: numero > 100,numeros))}")

print(f"FILTER en función LAMBDA que devuelve pares {list(filter(lambda numero: numero % 2 == 0,numeros))}")
#MAP genera una nueva lista con los resultados
print(f"Resultado de sumar 10 y dividir entre 2:{list(map(lambda x: (x+10)/2,numeros))}")

#Ejemplo de REDDUCE con una suma
print(f"Resultado: {reduce(lambda x, y : x +y, numeros)}") #REDUCE (función + iterable) aplica a los elementos la función lambda y los reduce a uno

#
print(f"Datos: {numeros}")
print(f"Pares: {list((map(lambda numero: numero % 2 == 0,numeros)))}")

print(f"¿Algún número par? {any((map(lambda numero: numero % 2 == 0,numeros)))}") #Any devuelve TRUE is alguna vez se cumple la condición
print(f"¿Algún número par? {any(numero % 2 == 0 for numero in numeros)}")

print(f"¿Todos los números pares? {all((map(lambda numero: numero % 2 == 0,numeros)))}") #All devuelve TRUE si siempre se cumple la condición

#################################################
#                    Yield                      #
#################################################

numeros = [8, 14, 65, 7, 14, 99, 745, 1, -35, 1408]

print(f"Datos: {numeros}")


def func1(lista): 
    for i in lista:
        return i*5 #Deuelve sólo el primer numero por 5
    
def func2(lista):
    resultado =[]
    for i in lista:
        resultado.append(i*5) #Devuelve todos los números multiplicados por 5 en una lista
    return resultado



print(f"Func1: {func1(numeros)}")
print(f"Func2: {func2(numeros)}")
print(f"Lambda: {list(map(lambda x: x *5, numeros))}") #Lo mismo que Línea14 más sencillo con lambda

def func3(lista):
    for i in lista:
        yield i*5 #Es como la función1 cambiando el retorno

print(f"Func3: {list(func3(numeros))}") #Es un objeto generador, hay que convertirlo a lista

#Utilización de los generadores
generador =func3(numeros)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

generador = func3(numeros)
for i in generador:
    print(f">> {i}")


try:
    generador2 = ((i * 5) for i in numeros)
    print(f">>> {next(generador2)} *")
    print(f">>> {next(generador2)} *")
    for i in generador2: #El generador seguirá por donde lo deja
        print(f">>> for: {i}")

    print(f">>> {next(generador2)} *")
except StopIteration as e:
    print(e)
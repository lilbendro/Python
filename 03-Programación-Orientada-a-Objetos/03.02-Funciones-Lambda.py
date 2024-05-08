#################################################
#              Funciones  Lambda                #
#################################################

def saludo(nombre):
    print(f"Hola, me llamo {nombre}")
miNombre = "Borja"

saludo(miNombre) #Dándole una variable como argumento
saludo("Francisco") #Dándole texto como argumento

#Una función Lambda equivvalente a la funcion saludo()
demo = lambda nombre : print(f"Hola, me llamo {nombre}") #Nombre variable = lambda + variable + funcionalidad
#La función se guarda como variable
print(f"Tipo de demo {type(demo)}") #Tipo función

miNombre = "Ana María"

demo(miNombre)
demo("Ana")

#Creamos una función Calcular() que recibe como parámetro una función lambada con el cálculo a realizar

def Sumar(num):
    return lambda a: a + num #Aquí "a" es el parámetro que está recibiendo

def Restar(num):
    return lambda a: a - num

def Multiplicar(num):
    return lambda a: a * num

def Dividir(num):
    return lambda a: a / num

def Calcular(formula): #Lo que hace la función calcular depende del Parámetro (función lambda)
    for n in range(1,11,1):
        print(f"Numero: {n} --> Resultado de la fórmula: {formula(n)}")

Calcular(Sumar(10))


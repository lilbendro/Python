#################################################
#            Conversión de Variables            #
#################################################

#Declaración de variables
a = 5.3
b = "25"
c = "25.7"
d = "a 8.4"

#Conversión de numero a texto con STR
print("El valor de A es: " + str(a)) #Como no se pueden concatenar variables numéricas y string, convertimos INT o FLOAT a STR
print("El valor de B es: " +b)
print("")

#Conversión de texto a número con INT y FlOAT.
print(f"Valor de B: {b}")
print(type(b))

print(f"Valor de B: {int(b)}") #Aquí con el formateador lo hemos convertido directamente a INT

print(f"Suma: {b+c}") #Se unen dos cadenas de texto
print(f"Suma: {int(b)+float(c)}") #Para sumarlos los convertimos a variable numérica. Hay que convertir C a float porque es decimal
print(type(int(a)+float(b))) #De sumar un INT y un FLOAT el resultado será un FLOAT

#Conversión de variables con letras y números
print(f"Numero: {d}") #Un STR que contiene letras no se pueden convertir a variable numérica.

#################################################
#             Sentencias de control             #
#               If / Elif / Else                #
#################################################

#Declaración de variables
a = 200
b = 33

#Ejemplo 1, IF/ELIF/ELSE
print(f"\n==Inicio del programa== \n")

if (b>a):
    print(f"B mayor que A")
    print(f"El valor de B es igual a {b}")
elif (a>b):
    print(f"A es mayor que B")
    print(f"El valor de A es igual {a}")
else:
    print(f"A es igual que B")

print(f"\n==Fin del programa==\n")

#Ejemplo 2 IF/ELIF
print(f"\n==Inicio del programa== \n")

if (b>a):
    print(f"B mayor que A")
    print(f"El valor de B es igual a {b}")
elif (a>b):
    print(f"A es mayor que B")
    print(f"El valor de A es igual {a}")
elif (a == b):
    print(f"A es igual que B")

print(f"\n==Fin del programa==\n")

#Ejemplo 3, IF/ELSE/IF/ELSE
print(f"\n==Inicio del programa== \n")

if (b>a):
    print(f"B mayor que A")
    print(f"El valor de B es igual a {b}")
else: 
    if (a>b):
        print(f"A es mayor que B")
        print(f"El valor de A es igual {a}")
    else:
        print(f"A es igual que B")

print(f"\n==Fin del programa==\n")
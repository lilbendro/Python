#################################################
#             Sentencias de control             #
#                      Try                      #
#################################################

#Declaración de variables
numero1 = 5
numero2= 100

#Ejemplo 1

print(f"Incio del programa\n")
try: 
    numero3 = numero2  /numero1
    print(f"Valor de numero 3: {numero3}")
except ZeroDivisionError:
    print(f"Error, división entre cero")
except:
    print(f"Error,excepción detectada")
else: 
    print(f"El bloque se ejecuta cuando el TRY finaliza correctamente")
finally:
    print(f"El bloque se ejecuta cuando el TRY o EXCEPT finalizan.")
print(f"\nFin del programa")

#Ejemplo 2

print(f"Incio del programa\n")
try: #Bloque de código que se prueba
    numero3 = numero2  /numero1
    print(f"Valor de numero 3: {numero3}")

    f = open("miFichero.txt") #Tratamos de abrir un fichero que no existe
except ZeroDivisionError as err: 
    print(f"{err}") #Pinta el mensaje de error
    print(f"{type(err)}") #Pinta la clase de error
except FileNotFoundError as err:
    print(f"{err}")
    print(f"{type(err)}")
except Exception as err: #Bloque de excepción genérica
    print(f"{type(err)}")

finally:
    print(f"\nFin del programa")

#Ejemplo 3 
numero = "32"

try:
    if(type(numero) is not int):
        raise Exception("La variable número no es numérica") #Creamos nosotros mismos la excepción con RAISE
except Exception as e:
    print(f"{e}")

#Try anidado
try:
    print("Nivel 1") #Si la excepción está en nivel 1 no ejecturá el nivel 2
    print("Inicio nivel 2")
    try:

        print("Nivel 2")
    except Exception as err:

        print(f"Nivel 2: {err}")
    finally: #Lo que está en FINALLY siempre se ejecuta
        print("Fin nivel 2")
except Exception as err:

    print(f"Nivel 1: {err}")
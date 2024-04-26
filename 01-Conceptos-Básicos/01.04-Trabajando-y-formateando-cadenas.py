#################################################
#            Trabajando y formateando           #
#              cadenas de carácteres            #
#################################################

#Declaración de variables
texto = "   Hola Mundo !!!   "
#Todas colecciones, incluidas las de caracteres, son de base 0: 01234567890123456789
print(texto)

#Mostrar determinados caracteres de la cadena
#Indicando su posición o un rango

print(f"Posición 3: {texto[3]}")
print(f"Desde la posición 3 inlcuida: {texto[3:]}")
print(f"Hasta la posición 6 NO incluida: {texto[:6]}")
print(f"Entre la posición 2 y 6, NO incluida: {texto[2:6]}")
print(f"Cuatro últimos caracteres empezando por la derecha: {texto[-5]}")

#Fucniones que podemos utilizar con las cadenas de texto
print(f"Contar número de caractéres: {len(texto)}")
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.strip()) #Elimina los espacios a principio y fin
print(texto.capitalize()) #Pone la mayuscula al comienzo de la frase (cuentan los espacios en blanco)
print(texto.title()) #Pone la mayuscula al comienzo de cada palabra
print(texto.count("o")) #Cuenta el número de letras
print(f"Es un dígito: {texto.isdigit()}") #IS admite muchos booleanos 
print(f"Es un digito: {"57".isdigit()}")

#Formatear cadenas de texto
mensaje = "Mundo"
print("Hola " + mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))
print(f"Hola {mensaje} !!!")

resultado = 10/3
print("Resultado: " + str(resultado))
print("Resultado: ", (resultado)) #La coma permite combinar variables numéricas y textuales
print(f"Resultado: {resultado}")
print("Resultado {r}".format(r=resultado))
print("Resultado {r:.2f}".format(r=resultado)) #.2f Limita el resultado a dos decimales
print(f"Resutlado:{resultado:.2f}")
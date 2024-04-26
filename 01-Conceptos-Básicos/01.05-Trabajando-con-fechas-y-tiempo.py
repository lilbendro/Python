#################################################
#        Trabajando con fechas y tiempo         #
#################################################

#Importamos los módulos
from datetime import datetime
import time
import locale #Para poner los nombre de día y mes en español 
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  #Configuración regional

#Declaración de variables
dt1 =datetime.now().date() #Creamos una variable de tipo DATE
print(f"Fecha 1: {dt1}")
dt1 =datetime.now() #Creamos una variable con el objeto DATETIME y su método NOW que captura la hora actual del sistema
print(f"Fecha 1: {dt1}")

#Mostramos parte de la fecha almacenada en la variable dt1
print("")
print(f"Día: {dt1.day}")
print(f"Día: {str(dt1.day).zfill(2)}") #zfill es un método que extiende la cadena a 2 carácteres, lo convertimos a STR porque es un método de las cadenas
print(f"Mes: {dt1.month}")
print(f"Mes: {str(dt1.month).zfill(2)}")
print(f"Año: {dt1.year}")
print(f"Hora: {dt1.hour}")
print(f"Minutos: {dt1.minute}")
print(f"Segundos: {dt1.second}")
print(f"Milisegundos: {dt1.microsecond}")

#Conversión de alfanumérico a fecha con STRPTIME (String Parse To time)
print("")
fecha = input("Escriba tu fecha de nacimiento (dd-mm-yyyy): ")
dt2 = datetime.strptime(fecha, "%d-%m-%Y").date() #Indicamos el formato según las variables de datetime. Retorna un date

#Mostramos la fecha sin formatear
print(f"Fecha 2: {dt2}")

#Monstramos la fecha formateada
print(f"La fecha es {dt2.strftime("%A, %d de %B de %Y")}") #STRFTIME para formatear la fecha + formato que se desea

#Cálculo de una fecha
print("")
    #Monstrainformación en TIMEDELTA (tiempo transcurrido)
dt2 = datetime.strptime(fecha, "%d-%m-%Y") #Para poder restar las fechas han de ser del mismo tipo, por lo que pasamos la dt2 a DATETIME
dtr = dt1 - dt2
print(type(dtr)) #El resultado de una resta de fechas será TIMEDELTA
print(dtr.days) #con DAYS se contarán los días transcurridos
print(dtr.seconds)
print(dtr.microseconds)

    #Opción 1
print(f"Tienes {dt1.year - dt2.year} años")

    #Opción 2
print("")
print(f"Tu edad es: {dtr.days/365.25}") #Edad con parte decimal
print(f"Tu edad es: {dtr.days//365.25}") #Edad sin parte decimal (entera)

    #Opción 3
edad = divmod(dtr.days, 365)            #Retorna el resultado y el resto en una tupla (colección cuyos valores no se pueden alterar)
print(edad)
print(f"Tienes {edad[0]} añós y {edad[1]} días")

    # Opción 4
print(f"Tienes {dtr.days // 365} años y {dtr.days % 365} días")

#Time retorna la cantidad de segundos transcurridos desde el comienzo (01-01-1970 00:00:00)
t1 = time.time()
print(f"Segundos desde 01-Ene-1970: {t1}\n")

#Transformación de segundos en una fecha
t2 = time.localtime(t1) #Con los segundos de T1 generamos la tupla 
print(f"Tupla: {t2}")
print(f"Año: {t2.tm_year} \n")

#Conversión de T2 en una representación de fecha y hora local
print(f"Fecha: {time.asctime(t2)} \n")
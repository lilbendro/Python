#################################################
#         Trabajando con zonas horarias         #
#################################################

#Importamos los módulos
from datetime import datetime 
import pytz 

#Mostrar las zonas horarias disponibles
print(pytz.all_timezones)
print("")

#Mostrar información sobre la fecha actual
dt = datetime.now()
print(f"Fecha: {dt}")
print(f"Zona horaria: {dt.tzinfo}") #No le hemos especificado la zona horaria y dará NONE
print("")

dtTokio =datetime.now(pytz.timezone("Asia/Tokyo")) #Seleccionamos la zona horaria
print(f"Fecha de Tokyo: {dtTokio}")
print(f"Zona horaria: {dtTokio.tzinfo}") #Nos arroja la zona horaria de Tokyo
print("")
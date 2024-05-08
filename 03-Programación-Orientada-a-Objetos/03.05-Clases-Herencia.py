#################################################
#                    Clases                     #
#                   Herencia                    #
#################################################

from datetime import datetime

class Alumno:
    """Clase demostración del curso de Python"""

    #Variables de clase / atributos
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    #Función constructora del objeto, se ejecuta al instancia el objeto
    #Self es una variable que contiene el propio objeto
    def __init__(self, nombre, apellido1, apellido2 = "") -> None: #None = no retorna nada
        self.Nombre = nombre #Establecemos correlación entre los parámetros de la función y los atributos del objeto
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2

    #Diversas funciones del objeto Alumno
    def getNombrecompleto(self) -> str: #GET para obtener datos del objeto. Retorna un STRING
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"
    
    def getEdad(self) -> int:
        try:
                resultado = datetime.now().date() - self.FechaNacimiento
                return int(resultado.days // 365.5)
        except:
            return -1
    def setFechaNacimiento(self, fecha) -> bool: #Set para grabar un dato. Retorna BOOL
        try:
            if (len(fecha) == 10): #Si me da una fecha de 10 dígitos
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            elif (len(fecha) == 8):#Si me da una fecha de 8 dígitos
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                return False

            return True
        except:
            return False
class Estudiante(Alumno): #Hereda de Alumno
    #Añadimos nuevas variables
    Curso = None

    #Sobrescribir funciones, por ejemplo el constructor
    def __init__(self, nombre, apellido1, curso) -> None:
        super().__init__(nombre, apellido1) #Con Super accedemos a la clase padre, y de su constructor sacamos lo que nos interesa
        self.Curso = curso #La funcionalidad que añadimos

    def getNombrecompleto(self) -> str:
        #return f"{self.Nombre} {self.Apellido1} {self.Apellido2} - Curso {self.Curso}"
        return f"{super().getNombrecompleto()} - Curso: {self.Curso}" #Retornamos el contenido heredado y añadimos algo nuevo
    
    #Añadimos nuevas funciones
    def test(self):
        return "Funcion test"

a = Alumno("Ana", "Sanz")
print(a.getNombrecompleto())

e = Estudiante("Borja", "Cabeza", "1ºA")
e.Nombre = "Francisco de Borja"
print(e.getNombrecompleto())
print(e.test())
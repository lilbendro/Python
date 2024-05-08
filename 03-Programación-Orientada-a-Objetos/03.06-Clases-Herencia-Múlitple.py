#################################################
#                    Clases                     #
#               Herencia Múltiple               #
#################################################

#Definición de la clase A
class A:
    Numero1 = None
    Numero2 = None
    def __init__(self) -> None:
        print("Constructor A")

    def Suma(self) -> int:
        return f"A  >> {str(self.Numero1 + self.Numero2)}"
    def Resta(self) -> int:
        return f"A  >> {str(self.Numero1 - self.Numero2)}"

#Definición de la clase B
class B:
    Numero1 = None
    Numero2 = None
    def __init__(self, n1, n2) -> None:
        self.Numero1 = n1
        self.Numero2 = n2
        print("Constructor B")

    def Suma(self) -> int:
        return f"B  >> {str(self.Numero1 + self.Numero2)}"
    def Resta(self) -> int:
        return f"B  >> {str(self.Numero1 - self.Numero2)}"
    def Multiplica(self) -> int:
        return f"B  >> {str(self.Numero1 * self.Numero2)}"
        
#Definimos la clase CALCULADORA que hereda de A y B
class Calculadora (A,B): pass #El orden en que hereda tiene importancia, A tendrá prelación en caso de variables o funciones homónimas

c = Calculadora()

c.Numero1 = 10
c.Numero2 = 15
print(f"Numero 1: {c.Numero1}")
print(f"Numero 2: {c.Numero2}")
print(f"Suma: {c.Suma()}")
print(f"Resta: {c.Resta()}")
print(f"Multiplica: {c.Multiplica()}")
#################################################
#                    Clases                     #
#               Miembros Privados               #
#################################################

#En Python todas las clases son públicas, se utiliza _ para definir lo privado
class Demo:
    __CLave = "12345678a"

    def publico(self):
        print("Todos pueden saber")
    
    def _privado (self):
        print ("Nadie debería saber")
    
    def __secreto(self): #__ renombrará el método o variable fuera del objeto y al buscarla no lo encontrará, simulando una "privacidad"
        print("Nadie puede saber")

    def getSecreto(self, pw): 
        if (pw == "1234"):
            self.__secreto() #Dentro del objeto podemos llamar a Secreto
        else:
            print("Sin acceso")

demo = Demo()
demo.publico()
demo._privado()

demo.getSecreto("1234")
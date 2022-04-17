import csv

class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDeDominio = ""
    __contraseña = ""
    
    
    def __init__(self,idc,dom,tipdom,contra):
        self.__idCuenta=idc
        self.__dominio=dom
        self.__tipoDeDominio=tipdom
        self.__contraseña=contra
           
    
    def retornaEmail(self, nombre):
        #print("Estimado " + nombre + "te enviaremos un mensaje a la direccion " + self.__idCuenta +"@"+ self.__dominio +"." + self.__tipoDeDominio)
        print("Estimado " + nombre + "te enviaremos un mensaje a la direccion " + self.__idCuenta+"@"+self.__dominio+"."+self.__tipoDeDominio)
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self, correo):
        adr=correo.split("@")
        tip=adr[1].split(".")
        self.idCuenta=adr[0]
        self.dominio=tip[0]
        self.tipoDeDominio=tip[1]
        
def modifica_contra(actual,oldpass):
        if actual == oldpass:
            actual=input("Ingrese nueva contraseña:")
            print("Su contraseña se modifico a: " + actual)
            return actual
        else:
            print("Contraseña incorrecta")


if __name__ == "__main__":

    ##APARTADO 1
    name= input("Ingrese nombre:")
    ##p = Email()
    ##p.crearMail()
    p = Email(input("Ingrese su ID:"), input("Ingrese su dominio:"), input("Ingrese su tipo de dominio:"), input("Ingrese su contraseña:"))
    p.retornaEmail(name)
    
    ##APARTADO 2
    p.contraseña = modifica_contra(input("Ingrese contraseña actual"),p.contraseña)
    
    ##APARTADO 3
    correo = Email()
    correo.crearCuenta(input("Ingrese correo"))
    print(correo.crearCuenta())
    
    ##APARTADO 4
    archivo = open("direcciones.csv")
    
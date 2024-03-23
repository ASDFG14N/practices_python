#En Python, los métodos get y set se utilizan en la programación orientada a objetos para controlar 
# el acceso a los atributos de un objeto.
#Estos metodos actuan sobre los campos, y los define como PRIVADOS.
#Su formato es el siguiente ==> self.__nombre_del_campo
# De esta manera se protegen ocultandolos del exterior, es decir el codigo que lo usa, impidendo ser 
#modificadps por el operador punto.Solo se pueden modificar desde dentro(de ahi lo de privados) de la clase.
#Esto se logra usando un metodo propio.

#El método set permite establecer el valor de un atributo privado de un objeto. 
#De esta manera, se puede controlar el valor que se le asigna a un atributo privado y asegurarse de que 
# cumpla con ciertas condiciones o restricciones.
#SET SE TRADUCE LITERALMENTE COMO COLOCAR

#El método get() permite obtener el valor de un atributo privado de un objeto. 
#En Python, por convención, los atributos privados se representan con un guión bajo al principio de su nombre 
#(ej. _atributo). Al utilizar el método get, se puede acceder al valor de un atributo privado sin 
# tener que acceder directamente a él.
#GET SE TRADUCE DIRECTAMENTE COMO OBTENER

class Ficha_Empleado:
    def __init__(self): #Metodo constructor __init__
        self.nombre = None #Atributos nombre
        self.edad = None #Atributo edad
        self.antiguedad = None #Atributo atiguedad 
        self.__cualificacion = None #Atributo __cualificacion ademas que queda protegido
    def sueldo(self):
        return (1000 + self.antiguedad*25 + self.__cualificacion*100)
    def setCualificacion(self, cualif: int): #Este metodo permite establecer el valor de la cualificacion
                                            #el empledado siempre que esté en el rano(1, 5), de no ser el caso
                                            #no se establecerá
        if cualif == 1 or cualif == 2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif
    def getCualificacion(self): #Este metodo devuelve el valor de la cualificacion
        return (self.__cualificacion)
def main():
    a = Ficha_Empleado()
    a.nombre = "Javier" 
    a.edad = 21
    a.antiguedad = 2


    #Establecemos a traves del metodo set un valor para el atributop privado cualificacion
    a.setCualificacion(3)
    a.setCualificacion(-7)
    a.setCualificacion(1.2)
    print("El sueldo de ", a.nombre, " con", a.antiguedad, " años en la empresa y su cualificacion de grado ", \
        a.getCualificacion() , " es de ", a.sueldo(), " euros" )
main()
#LOS PARENTESIS PARA LAS FUNCIONES SE PONEN PROQUE RETORNA UN VLAOR #

#A partir del ejemplo anterior si queremos comprobar que los datos cumplen los criterios impuestos desde un
#es conveniente definir determinados campos como privados y la forma de acceder a ellos es mediante metodos
#get y set definidos en la clase en custion, pero hay otra forma de hacerlo y se vera en el otro archivo.
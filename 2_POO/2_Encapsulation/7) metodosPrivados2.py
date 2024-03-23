class Ficha_Empleado:
    def __init__(self): #Metodo constructor __init__
        self.nombre = None #Atributos nombre
        self.edad = None #Atributo edad
        self.antiguedad = None #Atributo atiguedad 
        self.__cualificacion = None #Atributo __cualificacion ademas que queda protegido
    def __sueldo(self):
        return (1000 + self.antiguedad*25 + self.__cualificacion*100)
    def setCualificacion(self, cualif: int): #Este metodo permite establecer el valor de la cualificacion
                                            #el empledado siempre que esté en el rano(1, 5), de no ser el caso
                                            #no se establecerá
        if cualif == 1 or cualif == 2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif
    def getCualificacion(self): #Este metodo devuelve el valor de la cualificacion
        return (self.__cualificacion)
    def getSueldo(self):
        return self.__sueldo()
    
def main():
    a = Ficha_Empleado()
    a.nombre = "Javier"
    a.edad = 21
    a.antiguedad = 2
    a.setCualificacion(3)

    print("El sueldo de ", a.nombre, ", con ", a.antiguedad, \
          " años en la empresa y con cualificacion de grado ", a.getCualificacion(), \
            " es de ", a.getSueldo()," soles", sep="")
main()
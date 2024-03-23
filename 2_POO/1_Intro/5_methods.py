class Empleado():
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiguedad = None
        self.cualificacion = None
    def sueldo(self):
        return(1000 + self.antiguedad*25 + self.cualificacion*100)

def main():
    a = Empleado() 
    a.nombre = "Javier" 
    a.edad = 21
    a.antiguedad = 2
    a.cualificacion = 1

    b = Empleado()
    b.nombre = "Fernando" 
    b.edad = 32
    b.antiguedad = 9
    b.cualificacion = 4

    print("El sueldo de ", a.nombre, " con", a.antiguedad, " años en la empresa y su cualificacion de grado ", \
        a.cualificacion, " es de ", a.sueldo(), " euros" )
    print("El sueldo de ", b.nombre, " con", b.antiguedad, " años en la empresa y su cualificacion de grado ", \
        b.cualificacion, " es de ", b.sueldo(), " euros" )
    
main()
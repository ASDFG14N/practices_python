class Empleado:
    def __init__(self):
        self.nombre = None
        self.edad = None

def main(): 
    a = Empleado()
    a.nombre = "Javier"
    a.edad = 21

    b = Empleado()
    b.nombre = "Fernado"
    b.edad = 32

    b = a
    #7. luego de la ejecucion de esta linea b apuntara a al lugar en la memoria que ocupa a, veamos
    print(id(a))
    print(id(b))

    print(b.nombre)
    print(b.edad)

    b.nombre = "Fernado"
    print(a.nombre)

main()
class Empleado:
    num_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1

    @classmethod
    def contar_empleados(cls):
        print("El número total de empleados es:", cls.num_empleados)

empleado1 = Empleado("Juan", 30000)
empleado2 = Empleado("Ana", 35000)

Empleado.contar_empleados()
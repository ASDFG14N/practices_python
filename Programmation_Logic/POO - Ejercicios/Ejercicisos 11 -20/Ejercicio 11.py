#Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, 
#edad. Crea otra clase, Alumno, que herede de la primera estos atributos.
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
def imprimir(nombre, edad):
    print(f"El alumno {nombre} y tiene {edad} años")
alumnoUno = Alumno(nombre="Gian", edad="20")
alumnoDos = Alumno(nombre="Paola", edad="25")
imprimir(alumnoUno.nombre, edad=alumnoUno.edad)
imprimir(alumnoDos.nombre, edad=alumnoDos.edad)



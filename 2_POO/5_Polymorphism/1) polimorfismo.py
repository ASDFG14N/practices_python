class Vaca():
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice muuuu")
class Oveja():
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice meee")
#Instancias
vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

#en una funcion
def animalHablar(animal):
    animal.hablar()
animalHablar(vaca1)
animalHablar(oveja1)
class Persona:
    def __init__(self): #Metodo constructor o inicializador
        self.nombre = None #definicion del inicializador
        self.edad = None #definicion del inicializador


a = Persona()
print(a)
b = Persona()
print(b)

#-------------------------
a.nombre = "Javier"
a.edad = 21
print(a.nombre)
print(a.edad)
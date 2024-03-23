class Personaje():
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje(especie="Humano", magico="True", edad=17)
inuyasha = Personaje(especie="medio demonio", magico=False, edad=150)
print(f"Inuyasha es un {inuyasha.especie}")
print(f"Cuenta con poderes magicos?: {inuyasha.magico}")
print(f"Este personaje tiene {inuyasha.edad} años")
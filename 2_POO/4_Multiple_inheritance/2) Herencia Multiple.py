class cuadrado():
    def __init___(self, base):
        self.base = base
    @property
    def perimetro(self):
        return 4 * self.base
    @property
    def area(self):
        return self.base * self.base

class triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    @property
    def area(self):
        return 0.5 * self.base * self.altura

import math
#Creamos la clase piramide que va a heredar de cuadrado y truangulo
class Piramide(cuadrado, triangulo):
    def __init__(self, base, altura):
        super().__init___(base)  #Accedemos al cosntrucctor del cuadrado
        #Altura de la piramide
        self.altura = altura
    @property
    def altura_triangulo(self):
        return math.sqrt((self.base/2)** 2 + self.altura**2)
    @property
    def area(self):
        base_area = super().area
        base_perimetro = super().perimetro
        area_lateral = 0.5 * base_perimetro * self.altura_triangulo
        return area_lateral + base_area
    @property
    def volumen(self):
        base_area = super().area
        return (base_area * self.altura) / 3
def main():
    piramide = Piramide(2, 2)
    print(piramide.area)
    print(piramide.volumen)
main()



    
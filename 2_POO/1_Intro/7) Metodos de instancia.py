class Rectangulo():
    def __init__(self, base = 1, altura = 1, color = "azul"):
        self.base = base
        self.altura = altura
        self.color = color
    def perimetro(self): #Los metodos de instancia siempre deben tener el parametro "self"
        return 2*self.base + 2*self.altura
    def area(self):
        return self.base*self.altura
rectagulo_1 = Rectangulo(5, 2, "red")
print(f"El are del rectangulo es: {rectagulo_1.area()}")
print(f"El perimetro del rectagulo es: {rectagulo_1.perimetro()}")

rectagulo_1.base = 3
print(f"\nEl perimetro del rectagulo es: {rectagulo_1.perimetro()}")
print(f"El are del rectangulo es: {rectagulo_1.area()}")
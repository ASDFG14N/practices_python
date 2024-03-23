#cualquier llamada a un metodo usando super() no necesita el argumneto self

# Clase padre llamada Triángulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        """
        Constructor de la clase triángulo
        :param lado1: Lado 1 del triángulo
        :param lado2: Lado 2 del triángulo
        :param lado3: Lado 3 del triángulo
        """
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

# Subclase para calcular el perímetro del triángulo
class PerimetroTriangulo(Triangulo):
    def __init__(self, lado1, lado2, lado3): 
        """
        Constructor de la clase PerimetroTriangulo
        :param lado1: Lado 1 del triángulo
        :param lado2: Lado 2 del triángulo
        :param lado3: Lado 3 del triángulo
        """
        Triangulo.__init__(self, lado1, lado2, lado3) ##llamada al inicializador de la superclase

    def perimetro(self):
        """
        Método para calcular el perímetro de un triángulo
        :return: Perímetro del triángulo
        """
        return self.lado1 + self.lado2 + self.lado3

# Subclase para calcular el área del triángulo
class AreaTriangulo(Triangulo):
    def __init__(self, lado1, lado2, lado3):
        Triangulo.__init__(self, lado1, lado2, lado3)

    def area(self):
        """
        Método para calcular el área de un triángulo
        :return: Área del triángulo
        """
        # Se asume que la base y la altura se pueden calcular a partir de los lados del triángulo
        base = self.lado1
        altura = self.lado2
        return (base * altura) / 2
    
class MadianaTriangulo(Triangulo):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)
    def mediana(self):
        mediana = ((pow(self.lado1, 2) + pow(self.lado2, 2)) - (pow(self.lado3, 2) / 2)) / 2
        mediana = pow(mediana, 0.5)
        return mediana

def main():
    AreaTrianguloObj = AreaTriangulo(3, 5, 8)
    PerTrianguloObj = PerimetroTriangulo(3, 5, 8)
    MedTriaguloObj = MadianaTriangulo(3, 5, 8)
    print(f"El area de triangulo de lados 3, 5 y 8 es: {AreaTrianguloObj.area()}")
    print(f"El perimetro del triangulo de lados 3, 5 y 8 es: {PerTrianguloObj.perimetro()}")
    print(f"La mediana del triangulo de lados 3, 5 y 8 es: {MedTriaguloObj.mediana()}")
main()


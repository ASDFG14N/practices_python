class FiguraGeometrica: #Clase padre
    def __init__(self, radio):#constructor que define el atributo de la clase padre
        self.radio = radio

class Circulo(FiguraGeometrica): #Clase hija que hereda los atributos de la clase padre
    def __init__(self, radio):
        super().__init__(radio)

    def area(self):
        """Calcula y retorna el área del círculo."""
        return 3.14 * self.radio**2

    def perimetro(self):
        """Calcula y retorna el perímetro del círculo."""
        return 2 * 3.14 * self.radio

# Creación de un objeto círculo
circulo = Circulo(5)

# Cálculo y muestra del área
print("Área del círculo:", circulo.area())

# Cálculo y muestra del perímetro
print("Perímetro del círculo:", circulo.perimetro())
#En este ejemplo, la clase Circulo hereda de la clase FiguraGeometrica y sobreescribe los métodos area 
# y perimetro para calcular las medidas correspondientes a un círculo. También llama al constructor de la 
# clase padre en su propio constructor para inicializar el atributo radio.

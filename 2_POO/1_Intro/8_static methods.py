class Rectangulo():
    def __init__(self, base = 1, altura = 1, color = "blue"): #El constructor es llamado cuando se crea un objeto
        #de la clase.
        self.base = base
        self.altura = altura
        self.color = color
    def perimetro(self): #Los metodos de instancia siempre deben tener el parametro "self"
        return 2*self.base + 2*self.altura
    def area(self):
        return self.base*self.altura
    @staticmethod
    def son_iguales(rectangulo1, rectangulo2):
        if rectangulo1.base == rectangulo2.base and rectangulo1.altura == rectangulo2.altura:
            return True
        return False

rectangulo1 = Rectangulo(7, 5, "Verde")
rectangulo2 = Rectangulo(3+4, 7-2, "Azul")
print(Rectangulo.son_iguales(rectangulo1=rectangulo1, rectangulo2=rectangulo2))
#Estos se parecen a los "static void"  de java
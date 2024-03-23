import random
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
    @classmethod
    def random_rectangulo(cls):
        base = random.randrange(1,10)
        altura = random.randrange(1,10)
        return cls(base, altura)
    
rec3 = Rectangulo().random_rectangulo()
print(rec3.altura)
print(rec3.base)
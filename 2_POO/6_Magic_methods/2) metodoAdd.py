class Punto():
    def __init__(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y
    
    def __add__(self, otro):
        nuevo_x = self.eje_x + otro.eje_x
        nuevo_y = self.eje_y + otro.eje_y
        return Punto(nuevo_x, nuevo_y)

puntoA = Punto(8, 6)
puntoB = Punto(7, 10)
sumaDePuntos = puntoA + puntoB
print(sumaDePuntos.eje_x, sumaDePuntos.eje_y)

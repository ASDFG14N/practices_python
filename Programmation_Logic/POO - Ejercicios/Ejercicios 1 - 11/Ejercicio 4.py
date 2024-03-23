class OperacionesAritmeticas:
    def __init__(self, valorUno, valorDos):
        self.valorUno = valorUno
        self.valorDos = valorDos
    def suma(self):
        suma = self.valorUno + self.valorDos
        return suma
    def restaPositiva(self):
        if self.valorUno > self.valorDos: resta = self.valorUno - self.valorDos
        elif (self.valorUno < self.valorDos): resta = self.valorDos - self.valorUno
        return resta
    def resta(self):
        resta = self.valorUno - self.valorDos
        return resta
    def multiplicacion(self):
        producto = self.valorUno * self.valorDos
        return producto
    def division(self):
        cociente = self.valorUno / self.valorDos
        return cociente
class OperacionesAlgebraicas(OperacionesAritmeticas):
    def __init__(self, valorUno, valorDos):
        super().__init__(valorUno, valorDos)
    def potencia(self):
        potencia = 1
        for i in range(self.valorDos):
            potencia = potencia * self.valorUno
        return potencia
    def valorAbsoluto(self):
        if self.valorUno < 0: self.valorUno = self.valorUno * -1
        print(f"El valor asboluto es {self.valorUno}")


###############################################################################
valorabs = OperacionesAlgebraicas(-7, 9)
valorabs.valorAbsoluto()



    
        

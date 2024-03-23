class NumeroRacional():
    def __init__(self, numerdor, denominador = 1):
        if type(numerdor) is int and type(denominador) is int:
            self.numerdor = numerdor
            self.denominador = denominador
        else:
            print("El numerdor y denominador deben ser enteros")
    def __str__(self):
        return "{} / {}".format(self.numerdor, self.denominador)
    def mathFormat(self):
        from IPython.display import display, Latex
        display(Latex(f"${self.numerador}\\over{self.denominador}$"))

objeto = NumeroRacional(2, 5)
print(objeto)
objeto.mathFormat()
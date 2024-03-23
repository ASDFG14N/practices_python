class Casa():
    def __init__(self, color, cantidadPisos):
        self.color = color
        self.cantidadPisos = cantidadPisos
casaBlanca = Casa(color="Blanco", cantidadPisos=4)
print(f"La casa es de color {casaBlanca.color} y tiene {casaBlanca.cantidadPisos} pisos")
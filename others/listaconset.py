from random import choice
vehiculo = ["tren", "ferrocarril", "barco", "auto", "avion", "motocicleta", "autobus"]
palabraElegida = choice(vehiculo)
letraUnicas = len(set(palabraElegida))
print(palabraElegida)
print(letraUnicas)
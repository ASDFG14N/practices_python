#Si conoce el espacio total en un disco duro y también, el espacio ocupado, realice un programa que 
#calcule el porcentaje de espacio disponible.

print("\tEjercicio 28")
print("\t------------\n")

def calcular(total, ocupado):
    porOcupado = (ocupado / total)*100
    porDisponible = int(100 - porOcupado)
    return print(f"El espacio disponible es de {porDisponible}%")
def main():
    total = int(input("Introdusca el espacio total del disco duro: "))
    ocupado = int(input("Introdusca el espacio ocupado del disco duro: "))
    calcular(total=total, ocupado=ocupado)
main()

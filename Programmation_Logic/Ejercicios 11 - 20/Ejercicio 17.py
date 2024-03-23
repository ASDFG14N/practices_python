#Realice el algoritmo que permita sumar de manera algebraica los N términos siguientes:
#1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 + 1/7 - ...
#Primero, use la división modular. Después, utilice una bandera

print("\tEjercicio 15")
print("\t------------\n")

def sumatoria(n):
    sumatoria = 0
    for iterador in range(1, n+1):
        if iterador % 2 == 1:
            sumatoria = sumatoria + 1/iterador
        else:
            sumatoria = sumatoria - 1/iterador
    return sumatoria
n = int(input("Ingrese el número de términos a sumar: "))
resultado = sumatoria(n)
print("La suma de los", n, "términos es:", resultado)


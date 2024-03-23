#Implementar una función que calcule la suma de todos los números enteros comprendidos
#entre cero y un número entero positivo dado. (usando recursividad)
print("\tEjercicio 19")
print("\t------------\n")

def sumaRecursiva(num):
    if num == 0:
        return 0
    else:
        return num + sumaRecursiva(num-1)
def sumaFormula(num):
    return (num*(num+1)/2)
def sumatoria(num):
    sumatoria = 0
    for i in range(0, num+1):
        sumatoria = sumatoria + i
    return sumatoria

def main():
    print(f"La suma usando una funcion recursiva es: {sumaRecursiva(45)}")
    print(f"La suma usando la formula de sumas notables es: {sumaFormula(45)}")
    print(f"La suma usando programacion estructurada es: {sumatoria(45)}")
main()


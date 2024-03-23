#Desarrollar un algoritmo que permita calcular la siguiente serie:
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
print("\tEjercicio 22")
print("\t------------\n")

def serie(n):
    suma = 0
    contador = 1
    while contador <= n:
        suma = suma + 1/contador
        contador = contador + 1
    return print(f"El resultado de la serie hasta {n} como denominador es: {suma}")
n = int(input("Introduce un numero limite: "))
serie(n)
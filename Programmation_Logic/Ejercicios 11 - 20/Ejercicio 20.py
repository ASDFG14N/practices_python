#Implementar una función para calcular la potencia dado dos números enteros, el primero representa
#la base y segundo el exponente.
print("\tEjercicio 20")
print("\t------------\n")

def potencia(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * potencia(x, n - 1)
print(potencia(5, 3))
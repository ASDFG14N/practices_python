#factorial de un numero usando resursividad
print("\tEjercicio 18")
print("\t------------\n")
def factorial(numero):
    if numero == 0: #condicion de fin o caso base
        return 1
    else:
        return numero*factorial(numero-1)
#Una vez que se alcanza la condición de fin, se empiezan a resolver las llamadas recursivas previas
#que quedaron pendientes.
print(factorial(5))


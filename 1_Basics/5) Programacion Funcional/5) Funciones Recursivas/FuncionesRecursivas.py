#Las funciones recursivas tinen la capacidad de llamarse a si mismas, lo que se conoce como recursividad.
#La programacion recursiva, que hace uso de estas funciones, nos permiira resolver problemas que de la 
# forma habitual(progrmacion iterativa, bucles) seria muy complicado.
#Ejemplo de funciones recursivas, veamos el caso de un factoril. (Es comun en matematicas la definicion de 
# detrminadas funciones dividiendolas en dos partes:)
# 1. Un caso limite (0! = 1)
# 2. Un caso generico (n! = n * (n-1))
print("Recursividad en Programacion")
print("----------------------------\n")

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n* factorial(n-1))
def main(): #pide al usuario el numero e imprime pero va a la funcion facotrial
    a = eval(input("Introduce un entero positivo para calcualr su factorial: "))
    print("El factorial de ", a, "es: ", factorial(a))
main() #se ejecuta primero
#Observamos como en la definicion de la funcion factorial() se llama a ella misma con un argumento con una 
#unidad inferior

#Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
#se puede convertir el número a cadena.
print("\tEjercicio 23")
print("\t------------\n")

def suma_digitos(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + suma_digitos(num // 10)

num = 854
print("La suma de los dígitos de", num, "es:", suma_digitos(num))

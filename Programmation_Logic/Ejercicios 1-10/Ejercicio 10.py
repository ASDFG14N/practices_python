#Escribe un programa que diga si un número introducido por teclado es o no
#primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.

print("Ejercicio 8")
print("-----------\n")

def es_primo(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

n = int(input("Ingrese un número: "))
if es_primo(n):
    print(f"{n} es un número primo")
else:
    print(f"{n} no es un número primo")


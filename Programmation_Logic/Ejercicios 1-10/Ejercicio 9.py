#Escribe un programa que lea una lista de diez números y determine cuántos son positivos, y cuántos son negativos.

print("Ejercicio 9")
print("-----------\n")

contadorPositivos = 0
contadorNegativos = 0
for i in range(10):
    numero = int(input("Introduce un numero: "))
    if numero > 0:
        contadorPositivos = contadorPositivos + 1
    elif numero < 0:
        contadorNegativos = contadorNegativos + 1
print(f"El total de positivos es {contadorPositivos}")
print(f"El total de negativos es {contadorNegativos}")
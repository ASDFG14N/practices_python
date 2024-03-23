#Realiza un programa que sume los 100 números siguientes a un número entero
#y positivo introducido por teclado. Se debe comprobar que el dato introducido
#es correcto (que es un número positivo).

print("Ejercicio 11")
print("------------\n")

contador = 0
contador2 = 0
sumaTotal = 0
numero = int(input("Introduce un numero: "))
if numero>0:
    contador2 = numero + 1
    while contador<=100:
        sumaTotal = sumaTotal + contador2
        contador2 = contador2 + 1
        contador = contador + 1
else:
    print("El numero debe ser positivo")
print(sumaTotal)


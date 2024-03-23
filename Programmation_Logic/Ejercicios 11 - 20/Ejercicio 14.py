#Escribe un programa que muestre, cuente y sume los múltiplos de 3 que hay entre 1 y un número leído por teclado.
print("\tEjercicio 14")
print("\t------------\n")

contadorMultiplos = 0
sumaTotal = 0
numeroLimite = int(input("Introduce un numero: "))
for i in range(1, numeroLimite+1):
    if i%3 == 0:
        contadorMultiplos = contadorMultiplos + 1
        sumaTotal = sumaTotal + i
        print(i)

print("\nResultados")
print("El numero total de multiplos es:", contadorMultiplos)
print("La suma de multiplos es", sumaTotal)
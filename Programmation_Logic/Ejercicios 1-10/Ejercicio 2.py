#(Comparación de enteros) Escriba una aplicación que pida al usuario que escriba dos enteros, que obtenga
#los números del usuario y muestre el número más grande, seguido de las palabras “es más grande”. Si los números 
#son iguales, imprima el mensaje “Estos números son iguales”.

print("Ejercicio 2")
print("-----------\n")

numUno = int(input("Introduce el primer numero: "))
numDos = int(input("Introduce el segundo numero: "))

if numUno > numDos :
    print("El numero mas grande es", numUno)
elif numDos > numUno:
    print("El numero mas grande es", numDos)
else:
    print("Los numeros son iguales")
    
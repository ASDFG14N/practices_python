#(Aritmética) Escriba una aplicación que pida al usuario que escriba dos números, que obtenga los números
#del usuario e imprima la suma, producto, diferencia y cociente (división) de los números.
print("Ejercico #1")
print("-----------\n")

numUno = int(input("Introduce el primer numero: "))
numDos = int(input("Introduce el segundo numero: "))

suma = numUno + numDos
diferencia = numUno - numDos
producto = numUno * numDos
cociente = numUno / numDos

print("La suma es: ", suma)
print("La resta es: ", diferencia)
print("El producto es: ", producto)
print("El cociente es: ", cociente)
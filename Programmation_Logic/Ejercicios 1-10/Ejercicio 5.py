#(Par o impar) Escriba una aplicación que lea un entero y que determine e imprima si es impar o par [sugerencia:
#use el operador residuo. Un número par es un múltiplo de 2. Cualquier múltiplo de 2 deja un residuo de 0 cuando
#se divide entre 2].
print("Ejercicio 5")
print("-----------\n")

numero = int(input("Introduce un numero entero: "))
if numero % 2 == 0:
    print("En numero es par!!")
else:
    print("El numero es impar!")
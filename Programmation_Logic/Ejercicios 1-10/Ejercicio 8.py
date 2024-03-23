#Muestra la tabla de multiplicar de un número introducido por teclado.

print("Ejercicio 8")
print("-----------\n")

numero = float(input("Introduce un numero: "))
contador = 0
while contador<=10:
    print(f"{numero} x {contador} = {contador*numero}")
    contador = contador + 1
    

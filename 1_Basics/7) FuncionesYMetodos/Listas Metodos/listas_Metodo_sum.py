#El metodo sum permite sumar todos los elementos de una lista, esta lista debe conetener solo elementos numericos
#Sintaxis:
#sum(objeto_Iterable, valor_inicial) , este "valor_inicial" debe ser de tipo entero
#true = 1, false = 0
print("Metodo sum()")
print("----------\n")

numeros = [1, 2, 3]
print(f"Suma de los elementos de la lista: {sum(numeros)}")
print(f"Suma de los elementos de la lista con el argumento 4: {sum(numeros, 4)}\n")

a = range(1, 4)
print(sum(a))
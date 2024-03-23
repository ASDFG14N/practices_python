#Crear una lista con las palabras de una lista dada que tenga mas de 7 letras
untensilios = ["mesa", "interruptor", "silla", "microscopio", "cubo"]
listaSiete = [palabra for palabra in untensilios if len(palabra) > 7]
print(listaSiete)
#Crear una lista con el numero siguiente a los numeros de 1 al 30 que sean multiplos de 7 o 11
contiguos = [numero + 1 for numero in range(1, 31) if numero % 7 == 0 or numero % 11 == 0]
print(contiguos)
#Crea una lista en la que a partir de una dada se incluya el numero para y si es impar un cero
numeros = [2, 3, 5, 8, 9, 10, 12, 15]
#Si usamos la condicion else se usa anted del bucle for
pares = [n if n % 2 == 0 else 0 for n in numeros]
print(pares)
#Elabore el algoritmo que le permita obtener los mismos resultados
#que el protagonista de la anécdota de la suma del 1 al
#100. El algoritmo debe funcionar para obtener la suma entre
#cualquier par de números que sean inicio y final de la suma
#de números. Estos límites se circunscriben a dos casos: 1) el
#primer número debe ser impar y el segundo, par; 2) el primer
#número debe ser par y el segundo, impar. Pista: Puede usar
#una hoja de cálculo para hacer una simulación con dos listas
#de números para revisar el resultado de ambas y le servirá de
#guía para hacer el algoritmo.
print("\tEjercicio 29")
print("\t------------\n")

suma = 0
print("Usted tiene dos opciones a elegir:\n"
      "El primer número debe ser impar y el segundo, par (1)\n"
      "El primer número debe ser par y el segundo, impar (2).")
opcion = int(input("Introduca aquí su opcion: "))
numUno = int(input("Introduce el primer numero"))
numDos = int(input("Introduce el segundo numero"))
while numUno<=numDos:
    suma = suma + numUno
    numUno = numUno + 1
print("La suma es: ", suma)

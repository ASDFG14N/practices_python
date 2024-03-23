#Lectura de 20 elementos enteros de un vector denominado alfa.
print("\tEjercicio 24")
print("\t------------\n")

i = 1
alfa = []

numElementos = int(input("Ingrese el numero de elementos a ingresar: "))

while i <= numElementos:
    elemento = int(input(f"Ingrese el elemento del vector en la posicion #{i}: "))
    alfa.append(elemento)
    i = i + 1

print("La lista queda de la siguiente forma:")
print(alfa)

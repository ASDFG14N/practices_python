#Realiza un programa que pinte una pirámide por pantalla. La altura se debe pedir por teclado. 
# El carácter con el que se pinta la pirámide también se debe pedir por teclado.
print("Ejercicio 12")
print("------------\n")

n = int(input("Ingrese el número de filas: "))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

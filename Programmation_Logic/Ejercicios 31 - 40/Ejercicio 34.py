#Comprobar si un numero es perfecto, es decir la suma de sus divisores es igual al mismo numero
print("\tEjercicio 34")
print("\t------------\n")

def numeroPerfecto(numero):
    divisor, sumaDivisor = 0, 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisor = int (numero / i)
            sumaDivisor = sumaDivisor + divisor
    if sumaDivisor - numero == numero: print(f"El numero {numero} es perfecto")
    else: print(f"El numero {numero} no es perfecto")

numeroPerfecto(int(input("Introduce un numero: ")))

            

            

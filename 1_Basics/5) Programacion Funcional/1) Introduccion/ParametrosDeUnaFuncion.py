#Parametros de entrada y valor de salida de una funcion
#Haremos uso dde la instruccion especial return para retornar valores de salida
print("Parametros de entrada y valor de salida de una funcion")
print("------------------------------------------------------\n")

def calculo_de_datos(num1, num2):
    calculo = ((num1 - num2)*2) + 1
    return(calculo)
def main():
    for i in range(0,2):
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))
        resultado = calculo_de_datos(numero1, numero2)
        print("El primer numero introducido ha sido: ", numero1)
        print("El segundo numero introducido ha sido: ", numero2)
        print("El resultado de ellos es: ", resultado)
main()
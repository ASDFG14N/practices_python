#Una funcion puede recibir una serie de datos, procesarlos y devolver otra serie de datos como salida.
# El uso de return no esa limitado a un solo valor, en realida triene la capacidad de devolver multiples
# valore de salida mediante el siguiente formato ==> return valor_1, valor_2, valor_3, ...., valor_n
# Los valores "n" pueden ser variables o directamente expresiones.
print("Devolucion de multiples datos y argumentos por defecto en una funcion")
print("---------------------------------------------------------------------\n")

def calculadora(a, b):
    suma = a + b
    resta = a - b
    mutiplicacion = a + b
    return(suma, resta, mutiplicacion, a/b, a**b )
def main():
    print("Introduce dos valores sobre los que se haran  los calculos:")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    suma, resta, multiplicacion, division, potencia = calculadora(num1, num2)
    print("La suma es: ", suma)
    print("La resta es:", resta)
    print("La multiplicacion es: ", multiplicacion)
    print("La division es: ", division)
    print("La potencia es: ", potencia)
main()
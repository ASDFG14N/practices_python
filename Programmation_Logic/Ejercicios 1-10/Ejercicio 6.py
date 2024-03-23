#(Múltiplos) Escriba una aplicación que lea dos enteros, determine si el primero es un múltiplo del segundo e
#imprima el resultado. [Sugerencia: use el operador residuo].
print("Ejercicio 6")
print("-----------")
def Multiplos(x , y):
    if x % y ==  0:
        print(f"El numero {x} es multiplo de {y}")
    else:
        print(f"El numero {x} no es multiplo de {y}")
Multiplos(int(input("Introduce el primer valor: ")), int(input("Introduce el segundo valor: ")))
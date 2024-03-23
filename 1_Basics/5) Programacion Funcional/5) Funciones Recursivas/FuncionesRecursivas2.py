print("Recursividad en Programacion") #1
print("----------------------------\n") #2

def funcion1(n): #3 aloja en memoria esta funcion
    if (n >= 0):
        print(n, end= " => ")
        funcion1(n-1)
    else:
        print("Limite1")
def funcion2(n): #4 aloja en memoria esta funcion
    if (n >= 0):
        funcion2(n-1)
        print(n, end= " => ")
    else:
        print("Limite2")
print("Usando la funcion 1:") #5 Imprime en consola la frase
funcion1(10) #6 va a la funcion 1 tomando el valor de 10
print("Usando la funcion2:")
funcion2(10)

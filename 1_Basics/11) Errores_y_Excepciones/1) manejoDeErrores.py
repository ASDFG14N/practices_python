def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: ")) #hagamos que el usuario se equivoque y ponga una letra
    print(n1 + n2)
    print("Gracias por sumar" + n1) 
try:
    #codigo que queremos probar
    suma()
except TypeError:
    #codigo a ejecutar si no hay error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    #codigo a ejecutar si no hay error
    print("Hiciste todo correcto")
finally:
    #codigo que se va a ejecutar de todos modos
    print("Eso fue todo")
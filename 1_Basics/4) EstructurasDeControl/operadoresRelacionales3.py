#elif en python es a lo que en java seria la condicion else(sino)-if(si)
print("=========")
print("Conversor")
print("========= \n")

print("Menu de opciones: \n")
print("Presiona 1 para convertir de numero a palabra")
print("Presiona 2 para convertir de palabra a numero")

opcion = int(input("¿cual es tu opcion: "))
if opcion == 1:
    print("\n Conversor de numero a palabra. \n")

    opcion_1 = int(input("¿Cual es el numero que deseas convertir: "))

    if opcion_1 == 1:
        print("el numero es 'UNO'")
    elif opcion_1 == 2:
        print("el numero es 'DOS'")
    elif opcion_1 == 3:
        print("el numero es 'TRES'")
    elif opcion_1 == 4:
        print("el numero es 'CUATRO'")
    elif opcion_1 == 5:
        print("el numero es 'CINCO'")
    else:
        print("el numero seleccionado no esta registrado")

elif opcion == 2:
    print("\n Conversor de palabra a numero. \n")
    opcion_2 = input("Cual es la palabra?: ")
    if opcion_2 == "UNO" and "uno":
        print("el numero es '1'")
    elif opcion_2 == "DOS" and "dos":
        print("el numero es '2'")
    elif opcion_2 == "tres" and "TRES":
        print("el numero es '3'")
    elif opcion_2 == "cuatro" and "CUATRO":
        print("el numero es '4'")
    else:
        print("la palabra no esta registrada")

else:
    print("Opcion no disponible")

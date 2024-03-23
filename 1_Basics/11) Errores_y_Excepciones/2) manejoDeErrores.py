def pedirNumero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Es no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias, salimos del loop")
pedirNumero()
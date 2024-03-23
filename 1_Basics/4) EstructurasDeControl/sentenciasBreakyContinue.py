#Ejemplo para break

print("while con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5: #se detiene en el numero 5 y sale del ciclo
        break

    print("Valor actual de la variable: ", contador)

print("Fin del prgrama, la sentencia break se ha ejecutado.")

#Ejemplo para continue

print("\nwhile con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5: #solo se salta la condicion cuando 5 5, o sea no la imprime
        continue

    print("Valor actual de la variable: ", contador)
print("Fin del prgrama, la sentencia continue se ha ejecutado.")
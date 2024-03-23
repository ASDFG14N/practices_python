import random
print("\tEjercicio 38")
print("\t------------\n")
intentosRealizados = 0
print("¿Hola como te llamas?")
nombre = input()
numero = random.randint(1, 20)
print(f"Bueno {nombre} estoy pensando en un numero entre el 1 y 20")
while intentosRealizados < 6:
    print("Intenta adivinar el numero que pensé")
    estimacion = int(input("Escribe aqui tu respuesta: "))
    print()
    intentosRealizados = intentosRealizados + 1
    if (estimacion < numero):
        print(f"Tu estimacion es muy baja intentalo otra vez, te quedam {6 - intentosRealizados} intentos")
    if (estimacion > numero):
        print(f"Tu estimacion es muy alta, intentalo otra vez, te quedam {6 - intentosRealizados} intentos")
    if (estimacion == numero):
        break
if estimacion == numero:
    print(f"Buen trabajo {nombre}!!, lograste adivinar mi numero en {intentosRealizados} intentos")
else:
    print(f"Pues, no, el numero en el que estaba pensado era {numero}")


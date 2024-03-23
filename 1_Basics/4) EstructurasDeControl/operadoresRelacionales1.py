print("Sistema para calcular el promedio de un alumno")
nombre = input("Introduce tu nombre: ")
matematica = int(input(nombre + " ¿cual es tu nota de de matematicas?: "))
quimica = int(input(nombre + " ¿Cual es tu nota en quimica?: "))
fisica = int(input(nombre + " ¿Cual es tu nota en fisica?: "))

promedio = (matematica + quimica + fisica) / 3
promedio = int(promedio)
#codicion simple
if promedio >= 6:
    print('Felicidades ' + nombre + ' "¡APROBASTE!" con un promedio de: ', promedio)

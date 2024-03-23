print("Sistema para calcular el promedio de un alumno")
nombre = input("Introduce tu nombre: ")
matematica = float(input(nombre + " ¿cual es tu nota de de matematicas? "))
quimica = float(input(nombre + " ¿Cual es tu nota en quimica? "))
fisica = float(input(nombre + " ¿Cual es tu nota en fisica? "))

promedio = (matematica + quimica + fisica) / 3

#CONDICION COMPUESTA
if promedio >= 6:
    print('Felicidades ' + nombre + ' "¡APROBASTE!" con un promedio de: ', promedio)
    print('Felicidades ' + nombre + ' "¡APROBASTE!" con un promedio de: ', round(promedio,4))

else:
    print('Lo sentimos ' + nombre + ' "NO PROBASTE", tu promedio es de: ', promedio)
    print('Lo sentimos ' + nombre + ' "NO PROBASTE", tu promedio es de: ', round(promedio,6))

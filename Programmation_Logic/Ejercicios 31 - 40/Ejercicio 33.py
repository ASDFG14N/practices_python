#En un arreglo bidimensional se tienen almacenadas las calificaciones
#de diez alumnos en cuatro exámenes diferentes. Realice un programa que obtenga:
#a) El promedio de calificaciones de los diez alumnos en los cuatro exámenes.
#b) El alumno o alumnos que obtuvieron la mayor calificación en el tercer examen; en cualquier 
#caso debe imprimir cuántos alumnos fueron.
#c) El examen en el que el promedio del grupo fue el más alto.
#d) Cuántos alumnos están aprobados y cuántos reprobados, así como el porcentaje que representa.
import psutil
tuplaCalificaciones = ((20, 8, 9, 20), 
                       (19, 10, 6, 19), 
                       (18, 3, 10, 18), 
                       (10, 6, 9, 10), 
                       (19, 9, 10, 11), 
                       (15, 9, 18, 15), 
                       (15, 14, 15, 13), 
                       (20, 20, 19, 19), 
                       (20, 20, 12, 9), 
                       (17, 18, 16, 17))
#caso a)
def promedio():
    for i in range(0, 10):
        print(f"La el promedio de las calificaciones del alumno #{i + 1} es: {(sum(tuplaCalificaciones[i])/4)}")

#Caso b
def calMaxTercerExamen():
    CantSumaMin = 0
    for i in range(10):
        x = tuplaCalificaciones[i][2]
        if x >= 15:
            CantSumaMin = CantSumaMin + 1
    print("El numero de alumnos con puntaje mayor a 15 en el tercer examen es: ", CantSumaMin)

#Caso c)
def promGrupo():
    a, b, c, d = 0, 0, 0, 0
    promGrupo1 = 0
    for i in range(10):
        a = a + tuplaCalificaciones[i][0]
        b = b + tuplaCalificaciones[i][1]
        c = c + tuplaCalificaciones[i][2]
        d = d + tuplaCalificaciones[i][3]
    promPrimer = a / 10
    promSegundo = b / 10
    promTercer = c / 10
    promCuarto = d / 10
    listaNotaMax = [promPrimer, promSegundo, promTercer, promCuarto]
    if max(listaNotaMax) == promCuarto:
        promGrupo1 = 4
    elif max(listaNotaMax) == promTercer:
        promGrupo1 = 3
    elif max(listaNotaMax) == promSegundo:
        promGrupo1 = 2
    else:
        promGrupo1 = 1
    return (max(listaNotaMax), promGrupo1)

def main():
    print("Caso a)")
    print("-------")
    promedio()

    print("----------------------------------------------------------")

    print("\nCaso b)")
    print("-------")
    calMaxTercerExamen()

    print("----------------------------------------------------------")

    print("\nCaso c)")
    print("-------")
    listaNotaMax, promGrupo1 = promGrupo()
    print(f"El promedio máximo de los 4 exámens fue de: {listaNotaMax} y se dio en el #{promGrupo1}")
main()
process = psutil.Process()
print(f"Uso de memoria: {process.memory_info().rss / 1024 ** 2:.2f} MB")

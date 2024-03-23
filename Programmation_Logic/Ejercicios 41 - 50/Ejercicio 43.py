print("\tEjericio 43")
print("\t-----------\n\n")
def devolver_distintos(a, b, c):
    lista = [a, b, c]
    lista.sort()
    if lista[0] + lista[1] + lista[2] > 15:
        return lista[2]
    elif lista[0] + lista[1] + lista[2] < 10:
        return lista[0]
    elif lista[0] + lista[1] + lista[2] <= 15 or lista[0] + lista[1] + lista[2] >= 10:
        return lista[1]
print(devolver_distintos(2, 4, 2))


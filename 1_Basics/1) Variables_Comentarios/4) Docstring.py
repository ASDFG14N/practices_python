def division_euclidiana(x, y):
    '''
    Esta funcion calcula el cociente y el resto de la division entera de x entre y

    Args:
        x = int() dividendo
        y = int() divisor
    Returns:
        (q, r) son el cociente y residuo
    '''
    q = x // y
    r = x % y
    return q, r




#Con la ayuda del metodo doc podemos acceder directamente a la informacion indicada en el docstring de la
#funcion
print(division_euclidiana.__doc__)
print()
print(pow.__doc__)
print()
print(print.__doc__)
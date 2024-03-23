def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    else:
        return a / b

print(dividir(10, 0))

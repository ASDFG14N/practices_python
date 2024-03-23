#Crea un generador (almacenado en la variable generador) que sea capaz de devolver una 
#secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior 
#cada vez que sea llamada mediante next.
def secuenciaInfinita():
    x = 1
    yield x
    while True:
        x = x + 1
        yield x
generador = secuenciaInfinita()
print(next(generador))
print(next(generador))
print(next(generador))

print()

#Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera 
#indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado 
#devuelva el siguiente múltiplo (7, 14, 21, 28...).
def multiplos_siete():
    num = 1
    while True:
        yield 7*num
        num += 1

generadorDos = multiplos_siete()
print(next(generadorDos))
print(next(generadorDos))
print(next(generadorDos))
print(next(generadorDos))
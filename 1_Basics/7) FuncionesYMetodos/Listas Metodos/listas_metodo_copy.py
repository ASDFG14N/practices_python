print("El metodo copy()")
print("----------------\n")
listaNumeros = [1, 2, 3]
listaNumeros2 = listaNumeros
print("listaNumeros2 es listaNumeros?", listaNumeros2 is listaNumeros)
listaNumeros2[0] = 10
print("La listaNumeors ahora es: ", listaNumeros)

listaNumeros2 = listaNumeros.copy()
print("listanumeros2 es listaNumeros?: ", listaNumeros2 is listaNumeros)
listaNumeros[0] = 1
print("listaNumeros: ", listaNumeros)
print("listaNumeros2: ", listaNumeros2)
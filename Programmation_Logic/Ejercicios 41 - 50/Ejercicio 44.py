print("\tEjericio 44")
print("\t-----------\n\n")
def recibirPalabra(palabra):
    lista = list(set(palabra))
    lista.sort()
    return lista
print(recibirPalabra("entretenido"))

#Eliminar una lista – La instrucción del
#Este metodo permite eliminar toda una lista, y a su vez perminte eliminar un unico elemento indicando la
#la posicion exacta del elemento
#sintaxis: del nombre_lista[posicion]
#Si se desea eliminar mas de un elemento la sintaxis es la siguiente ==> del nombre_lista[posicionInicial:posicionFinal]
print("La instruccion del...[]")
print("-----------------------")

consonantes = [ "b", "c", "e", "t", "z"]
print(f"Lista: {consonantes}")
del consonantes[2]
print(f"del consonantes[2]: {consonantes}")

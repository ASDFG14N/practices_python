#El metodo index perminte localizar elemntos dentro de una lista, dicho metodo devolvera un valor de tipo
#entero, el cual representa el incice de la primera coincidencia del elemtndo especificado a encontrar.
#Sintaxis:
#1. nombre_lista.index(elemento) ==> el "elemtento", es el elemtndo que se desa buscar dentro de la lista
#2. nombre_lista.index(elemento, inicio) ==> el inicio inidica la posicion desde donde se va a comenzar a buscar el elemento
#3. nombre_lista.index(elemento, inicio, final) ==> final inicia el final, hasta donde se buscara el elemento.
vocales = ["a", "e", "i", "o", "u"]
print(f"Lista: {vocales}")
print(f"La letra a esta en la posicion numero: {vocales.index('a')}")
print(f"La letra i esta en la posicion numero: {vocales.index('i')}")
print(f"La letra u en el rango [2-final], esta en la posicion numero: {vocales.index('u', 2)}")
print(f"La letra i en el rango [2-4], esta en la posicion numero: {vocales.index('i', 2, 4)}")
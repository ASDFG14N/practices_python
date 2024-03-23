#Eliminando elemntos de un lista, metodo pop()
#Sistaxis: nombre_la_lista.pop(), cuando no se pasa ningun argumento se elimina el ultimo elemento
#generalmente se pasa un argunento que seria la posicion de la lista del elemento que se quiere eliminar, por ejemplo:
#sintaxis: nombre_lista.pop(posicion)
print("Eliminar elementos de una lista usando el metodo pop()")
print("------------------------------------------------------")
vocales = ["a", "e", "i", "o", "u"]
print(f"Lista: {vocales}")
print(f"Elemento eliminado: {vocales.pop()}")
print(f"Lista: {vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocales}")
print(f"Elemento eliminado en la posición 2: {vocales.pop(2)}")
print(f"Lista: {vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocales}")
print(f"Elemento eliminado en la posición 0: {vocales.pop(0)}")
print(f"Lista: {vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocales}")
print(f"Elemento eliminado en la posición -2: {vocales.pop(-2)}")
print(f"Lista: {vocales}")
print("")
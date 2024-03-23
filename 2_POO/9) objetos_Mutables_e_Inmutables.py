#recordemos que todo en python son objetos. Al trabajar con numeros enteros, reales, caracteres.Todos ellos son 
# ejemplos de de objetos INMUTABLES, pues su contenido no puede cambiar. tambien es bueno recordar que python
# clase es sinonimo de de TIPO, por lo que podemos pensar en los numeros enterors, reales, cadenas de caracteres
# como objetos de tres clases, int float, str. Los objetos creados a partir de nustras clases a medida son 
# MUTABLES, ya que pueden cambiar su valor.

#En Python, los objetos INMUTABLES se comportan de manera diferente a los objetos MUTABLES cuando son pasados 
# a funciones.

# Si un objeto IMNUTABLE se pasa como argumento a una función, la función no puede cambiar su valor. En cambio, 
# sólo puede crear una nueva versión modificada del objeto y devolverla.
#objetos inmutables (por ejemplo, números, cadenas, tuplas)

#Si se pasa un objeto MUTABLE a una función, cualquier cambio realizado a ese objeto dentro de la función se 
#reflejará en el objeto original. Esto se debe a que los objetos mutables se pasan por referencia en Python.
#Objetos mutables (por ejemplo, listas, diccionarios, conjuntos) 





#Ejemplo de objeto MUTABLE
print("Objeto Mutable")
def modificar_lista(lista): #Creamos la funcion modificar_lista() y retorna la lista modificada
  lista.append(4)
  return lista

mi_lista = [1, 2, 3] #Definimos la lista con sus elementos
nueva_lista = modificar_lista(mi_lista)#creamos un objeto nueva_lista
print(mi_lista) # [1, 2, 3, 4] #IMPRIMIMOS LA LISTA ORIGINAL
print(nueva_lista) # [1, 2, 3, 4] 3IMPRIMIMOS LA NUEVA LISTA

#En este ejemplo, la función modificar_lista() añade un elemento a la lista que se le pasa como argumento, 
# y como resultado, ambas listas (la original y la nueva) contienen el mismo elemento adicional.
print()


#Ejemplo de objeto inmutable
print("Objeto Inmutable")
def modificar_numero(numero): #Definimos una funcion
  numero += 1
  return numero

mi_numero = 5
nuevo_numero = modificar_numero(mi_numero)
print(mi_numero) # 5
print(nuevo_numero) # 6
#En este caso, la función modificar_numero devuelve un nuevo número que es una versión modificada del 
# original, pero el valor original del número no ha cambiado.
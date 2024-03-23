#¿De que tipo son los datos? Usaremos la funcion type() para verificar
a = 2
b = 7.52
c = "Texto"
d = False
print("El tipo de dato de ", a, " es ", type(a))
print("El tipo de dato de ", b, " es ", type(b))
print("El tipo de dato de ", c, " es ", type(c))
print("El tipo de dato de ", d, " es ", type(d))
#como vemos el interprete de python nos devuelve el tipo de dato pero con la palabra "class".
#Python basa su concepto de POO en que cualquier dato es un objeto de una determinada clase, siendo clase
#sinonimo de tipo en este caso, es decir, 2,7,21 son datos de tipo entero o lo que es lo mismo, objetos de la 
#clase int

#La funcion id() nos devuelve el identificador del objeto pasado como argumento
print("\nIdentificadores")
print("El posicion exacta de la memoria donde esta almacenado el objeto", a, " es ", id(a))
print("El posicion exacta de la memoria donde esta almacenado el objeto", b, " es ", id(b))
print("El posicion exacta de la memoria donde esta almacenado el objeto", c, " es ", id(c))
print("El posicion exacta de la memoria donde esta almacenado el objeto", d, " es ", id(d))
print()

#Un objeto de determinada clase haciendo uso de un metodo de la misma, es decir, los objetos que pertenecen a una
#clase pueden hacer uso de los metodos que pertenescan a la misma.

e = "ejemplo" #se crea el objeto "ejemplo", la variable e apunta a el.
i = "EJEMPLO" #se crea el objeto "EJEMPLO", la variable i apunta a el.
print(id(e))
print(id(i))
e = e.upper() #Se crea un nuevo objeto "EJEMPLO", la variable e apunta a el
print(id(e)) #Se alija en otro lugar de la memoria
f = "ejemplo" #f apunta al objeto ya creado
print(id(f)) #como vemos no cambio el lugar en la memoria

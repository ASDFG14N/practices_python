#En el ejemplo anterior se definió una variable global fuera de todas las funciones y luego desde las dos funciones
#enlazamos a esa variable global mediante el uso de global. Tambienn es posible crear una variable global 
#directamente desde las funciones sin hacerlo fuera de ella y basta con indicarlo con global.
def funcion2():
    global x
    x = 100
    x = x + 5
    print("La variable x dentro de la funcion2 vale: ", x) #105
def main(): #2
    funcion2()
    global x
    x = x + 10
    print("La variable dentro de main vale: ", x) #115
main() #1
#Resaltar que el uso de global en las dos funciones impresindible para trabajar con la misma variable
#De no haber declarado como global a x en el main podriamos haber creado otra variable local llamada x y seria
#un caso de coexistencia variables con el mismo nombre, una global y otra local
#global nos permite:
# - Trabajar en nuestra funcion con varables ecistentes en el ambito global
# - crear en nuestras funciones variables globales
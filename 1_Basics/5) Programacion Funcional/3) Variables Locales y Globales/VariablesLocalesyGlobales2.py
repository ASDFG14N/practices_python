x = 5 
def funcion2():
    global x
    x = x + 5
    print("La variable dentro de la funcion2 vale: ", x)
def main():
    global x
    x = x + 10
    funcion2()
    print("La variable dentro de main vale: ", x)
main()
#vemos que ambas funciones arrojan 20. Mediante el global x indicamos que esa x con la que trabajamos a nivel
#local es definida a nivel global, en la linea 8 al valor original le suma 10, hasta ahi tenemos 15. 
# Posteriormente en la linea 4 se le suma 5, tenemos 20, imprime eso en pantalla, termina su ejecucion y va al 
#print de la funcion main() como actuamos siempre con la misma varable, sacaran el mismo resultado
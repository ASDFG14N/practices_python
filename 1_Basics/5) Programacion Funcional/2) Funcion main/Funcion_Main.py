#Nos surge la duda de donde se define la funcion y como distinguimos el codigo de ésta respecto al programa
# principal. Todo lo que escribimos en el editos de codigo es el programa principal, por lo que no hace
# falta indicarlo de ninguna manera. Pero al usar funciones se debe indicar qué es qué.
# Para ello el programa principal sera una funcion de nombre main(). Para nosotros ejecutar un programa 
# ejecutaremos el main(), que sera el que posteriormente llame a las demas funciones.#

def calculo_de_la_mutiplicacion():
    numero1 = int(input("Introduce el primer numero: "))
    numero2 = int(input("Introduce el segundo numero: "))
    resultado = numero1 * numero2
    print(f"Haz introduciodo el numero: {numero1}")
    print(f"Haz introducido el segundo numero: {numero2}")
    print(f"El producto entre ellos es: {resultado}")

def main():  #Hemos definido la funcion pricipal y luego la vamos a ejecutar. Las funciones iran definidas 
             # encima de la definicion main, ya que ésta va hacer uso de ellas y deben estar cargadas en meoria
    for i in range(0,3):
        calculo_de_la_mutiplicacion()

main() #Ejecutando la funcion main()

#Explicacion:
#Definimos la funcion main y la del calculo, luego ejecutamos main() que es el programa principal, que 
#seguidamente llamara tres veces a la funcion calculo. Definir una funcion principal main desde que 
#arranca todo el programa es un convenio
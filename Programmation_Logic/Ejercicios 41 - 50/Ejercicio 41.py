import random
#Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados 
#(la función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

#Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
#(es decir, esta segunda función debe recibir dos argumentos) y que retorne un mensaje según la suma 
#de estos valores:

#Si la suma es menor o igual a 6:
#       "La suma de tus dados es {suma_dados}. Lamentable"
#Si la suma es mayor a 6 y menor a 10:
#       "La suma de tus dados es {suma_dados}. Tienes buenas chances"
#Si la suma es mayor o igual a 10:
#       "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
#utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
print("\tEjericio 41")
print("\t-----------\n\n")

def lanzar_dados():
    dado1 = random.randint(1, 6) #Lanza el primer dado
    dado2 = random.randint(1, 6) #Lanza el segundo dado
    return dado1, dado2 #Retorna el valor del primer y el segundo dado

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dado1, dado2 = lanzar_dados()
print(f"Los resultados de los dados son: {dado1} y {dado2}")
print(evaluar_jugada(dado1, dado2))

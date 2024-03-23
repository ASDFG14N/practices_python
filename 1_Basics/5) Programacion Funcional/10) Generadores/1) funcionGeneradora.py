print("Funciones Generadoras")
print("-" * 21 + "\n\n")

#Supongamos que necesitamos una funcion que retorne una lista de numeros del 1 al 4 multiplicados por 10

#funcion normal
def funcionNormal():
    lista = []
    for x in range(1, 5):
        lista.append(x*10)
    return lista
#funcion generadora
def funcionGeneradora():
    for x in range(1, 5):
        yield x * 10

print(funcionNormal()) #retorna una lista
print(funcionGeneradora()) #ya creo la lista, pero sin datos en el

#creamos una variable
generado = funcionGeneradora()
print(next(generado)) #retorna el primer numero
print(next(generado)) #retorna el segundo numero, simpre recueda donde se quedo
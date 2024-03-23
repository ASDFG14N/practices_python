from random import choice
print("\tJUEGO: EL AHORCADO")
print("\t------------------\n")
imagenes = ['''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
       |
       |
       |
       |
=========''']
#Lista de palabras
palabras = ["humanidad", "humano", "persona" ,"gente" ,"hombre" ,"mujer", "niño", "niña",
            "adolescente", "adulto", "adulta", "anciano", "anciana", "señor", "señora", "caballero",
            "dama", "abdomen", "cuello", "mente"]
animales = [ "perro", "gato", "vaca", "cerdo", "oveja", "caballo", "yegua", "mono", " rata", "tigre", 
            "conejo", "ciervo", "rana", "jirafa", "elefante", "gallina", "cuervo", "pez"]
hogar = ["escritorio", "silla", "mesa", "cama", "dormitorio", "oficina", "puerta", "ventana", 
         "escalera", "ascensor"]
vehiculo = ["tren", "ferrocarril", "barco", "auto", "avion", "motocicleta", "autobus"]
#Variables
letrasCorrectas = []
letrasIncorrectas = []
intentos = 7
aciertos = 0
juegoTerminado = False #indica el final del juego, inicia como falso

#funciones
#Esta funcion elige una tematica
def elegirTematica():
    print("Elige una tematica")
    print("1) Aleatorio\n2) Animales\n3) Objetos del hogar\n4)Vehiculos de trasporte")
    tematica = int(input("Tu respuesta aquí: "))
    if tematica == 1:
        return palabras
    elif tematica == 2:
        return animales
    elif tematica == 3:
        return hogar
    elif tematica == 4:
        return vehiculo
#funcion que elije una palabra al azar de la tematica elegida en la funcion anterior
#toma como parametro culquiera de las cuatro listas
def elegirPalabra(listaPalabras):
    palabraElegida = choice(listaPalabras) #la funcion choice retorna cualquier palabra de la lista y lo
    #asigna a la variable palabraElegida
    letrasUnicas = len(set(palabraElegida))
    #Esta variable es en numero de elementos que presenta el conjunto creado a partir de una palabra de la 
    # lista sin repetir letras
    return palabraElegida, letrasUnicas

#funcion que pide al usuario una letra cualquiera
def pedirLetra():
    letraElegida = ""
    esValida = False #hasta que no eliga la letra correcta la variable sera falsa
    #la varible abecedario comprueba con letra elegida si es una letra del abecedario
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    while not esValida: # El bucle se repita tantas veces como la letra no es valida, en este caso es True
        letraElegida = input("Elije una letra: ")
        letraElegida = letraElegida.lower() #transforma la letra a minuscula en caso sea mayuscula
        # si letraElegida esta en abcedario Y el tamaño deletraElegida es 1
        if letraElegida in abecedario and len(letraElegida) == 1:
            #Si es verdadera, esValida sera verdadera
            esValida = True
        else:
            print("La letra es incorrecta")
    return letraElegida
#funcion que se encarga de mostrar el tablero
def mostrarTablero(palabraElegida):
    listaPalabraOculta = []
    for letra in palabraElegida:
        if letra in letrasCorrectas:
            listaPalabraOculta.append(letra)
        else:
            listaPalabraOculta.append("_")
    print("Palabra Oculta: [ " + " ".join(listaPalabraOculta) + " ]")
#funcion que chequea si la letra escrita es correcta
def verificarLetraCorrecta(letraElegida, palabraOculta, vida, coincidencias):
    fin = False
    if letraElegida in palabraOculta:
        letrasCorrectas.append(letraElegida)
        coincidencias = coincidencias + 1
    else:
        letrasIncorrectas.append(letraElegida)
        print(imagenes[vida - 1])
        vida = vida - 1
    if vida == 0:
        fin = perder()
    elif coincidencias == letrasUnicas:
        fin = ganar(palabraOculta)
    return vida, fin, coincidencias
def perder():
    print("No hay mas vidas")
    print("La palabra correcta era:", palabra)
    return True
def ganar(palabraDescubierta):
    mostrarTablero(palabraDescubierta)
    print("¡Ganaste el juego!")
    return True
palabra, letrasUnicas = elegirPalabra(elegirTematica())
#Llamado de las funciones
while not juegoTerminado:
    mostrarTablero(palabra)
    print("Letras incorrectas: " + "-".join(letrasIncorrectas))
    print(f"Vidas Restantes ♥: {intentos}")
    letra = pedirLetra()
    print("*" * 20)
    intentos, terminado, aciertos = verificarLetraCorrecta(letraElegida=letra, 
                                                           palabraOculta=palabra, 
                                                           vida=intentos, 
                                                           coincidencias=aciertos)
    juegoTerminado = terminado
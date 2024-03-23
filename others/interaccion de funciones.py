from random import shuffle
#lista inicial
palitos = ["-", "--", "---", "----"]
#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista
#pedir intento
def probar_suerte():
    intento = ""
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Escribe un numero de 1 al 4: ")
    return int(intento)
#coprobar intento
def chequear_intento(lista, intento):
    if lista[intento-1] == "-":
        print("A lavar los platos")
    else:
        print("Te salvaste, no lavaras los platos")
    print(f"Te toco {lista[intento-1]}")
palitosMezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(lista=palitosMezclados, intento=seleccion)
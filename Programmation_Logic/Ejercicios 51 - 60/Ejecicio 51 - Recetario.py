import os
from pathlib import Path
from os import system

ruta = Path(Path.home(), "Desktop", "Recetas")

#mostrar cuantas recetas hay
def contarRecetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador = contador + 1
    return contador

#menu de inicio
def inicio():
    system("cls")
    print("*" * 38)
    print("Bienvenido al administrador de recetas")
    print("*" * 38)
    print(f"\nLa recetas se encuentran en {ruta}")
    print(f"Total recetas: {contarRecetas(ruta=ruta)}")
#Tenemos que mostrar el menu de opciones, como este menu debe mostrarse una y otra vez mietras
#que el usuario no elija la opcion correcta
    eleccionMenu = "x"
    while not eleccionMenu.isnumeric() or int(eleccionMenu) not in range(1, 7):
        print("Elige una opcion:")
        print('''
        [1] - LEER RECETAS
        [2] - CREAR RECETA NUEVA
        [3] - CREAR CATEGORIA NUEVA
        [4] - [ELIMINAR RECETA]
        [5] - ELIMINAR CATEGORIA
        [6] - SALIR DEL PROGRAMA''')
        eleccionMenu = input("Tu opcion aquí: ")
    return (eleccionMenu)

def mostrarCategorias(ruta):
    print("Categorias:")
    rutaCategorias = Path(ruta)
    listaCategorias = []
    contador = 1
    for carpeta in rutaCategorias.iterdir():
        carpetaSrt = str(carpeta.name)
        print(f"[{contador} - {carpetaSrt}]")
        listaCategorias.append(carpeta)
        contador = contador + 1
    return listaCategorias
import numeros

def preguntar():
    print("Bienvenido a bituque python")
    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break
    numeros.decorador(rubro=rubro)
def main():
    while True:
        preguntar()
        try:
            otroTurno = input("Quieres otro turno? [S] or [N]: ").upper()
            ["S", "N"].index(otroTurno)
        except ValueError:
            print("Es no es una opcion valida")
        else:
            if otroTurno == "N":
                print("Gracias por su visita")
main()
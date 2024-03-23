#generadores
def numerosPerfumeria():
    for n in range(1, 1000):
        yield f"P - {n}"
def numerosFarmacia():
    for n in range(1, 1000):
        yield f"F - {n}"
def numerosCosmeticos():
    for n in range(1, 1000):
        yield f"C - {n}"
perfumeria = numerosPerfumeria()
farmacia = numerosFarmacia()
cosmeticos = numerosCosmeticos()

#decorador
def decorador(rubro):
    print("\n" + "*" * 23)
    print("Su numero es:")
    if rubro == "P":
        print(next(perfumeria))
    elif rubro == "F":
        print(next(farmacia))
    else:
        print(next(cosmeticos))
    print("Será atendido en unos momentos")
    print("\n" + "*" * 23)
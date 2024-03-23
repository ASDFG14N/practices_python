#Dada una secuencia de caracteres, obtener dicha secuencia invertida.
print("\tEjercicio 20")
print("\t------------\n")

def invertir(caracter):
    string = str (caracter)
    stringReverso = ""
    for i in string:
        stringReverso = i + stringReverso
    return print(f"La lista de caracteres '{caracter}' al revés es: '{stringReverso}'")
def main():
    caracteres = input("Introduce una cadena de caracteres: ")
    invertir(caracteres)
main()


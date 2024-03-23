#en esta misma clase Palindromo, añada un atributo que se inicializará en el constructor.
#Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo.
#Además, al destruir la instancia, muestre el atributo en mayúsculas
print("\tEjercicio 2")
print("\t-----------\n")

class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra
    def __del__(self):
        print(self.palabra.upper())
    def test(self):
        return Palindromo.esPalindromo(self.palabra)
    #Metodo de la clase que verifica si una cadena es palindromo
    def esPalindromo(palabra):
        if len(palabra) <= 1: #Una cadena de nungun caracter o un caracter es palindromo
            return True
        
        #si el primer y ultimo caracter son iguales, y si la subcadena restante es ella misma un palindromo,
        #Entonces toda la cadena es un palindromo
        return palabra[0] == palabra[-1] and Palindromo.esPalindromo(palabra[1:-1])
    
p = Palindromo("radar")
print(p.test())
p = Palindromo("sonar")
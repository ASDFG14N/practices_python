#crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve
#un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. 
#Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. 
#Se tienen en cuenta los caracteres no alfanuméricos.

print("\tEjercicio 1")
print("\t-----------\n")

class Palindromo:
    #Metodo de la clase que verifica si una cadena es palindromo
    def esPalindromo(palabra):
        if len(palabra) <= 1: #Una cadena de nungun caracter o un caracter es palindromo
            return True
        
        #si el primer y ultimo caracter son iguales, y si la subcadena restante es ella misma un palindromo,
        #Entonces toda la cadena es un palindromo
        return palabra[0] == palabra[-1] and Palindromo.esPalindromo(palabra[1:-1]) 
print(Palindromo.esPalindromo("lol"))
print(Palindromo.esPalindromo("ArdeyalayedrA"))
print("ArdeyalayedrA"[1:-1])
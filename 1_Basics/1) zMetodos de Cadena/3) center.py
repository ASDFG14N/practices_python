#Devuelve una cadena centrada
#Sintaxis: string.center(length, character)
#length: Requerido. La longitud de la cadena devuelta.
#character: Opcional. El carácter para llenar el espacio que falta en cada lado. El valor predeterminado es " " (espacio)
print("Metodo Center")
print("-------------\n")

#Ejemplo
#Escriba la palabra "banana", ocupando el espacio de 20 caracteres, con "banana" en el medio:
txt = "banana"
x = txt.center(20)
print(x)

print()

txt = "banana"
x = txt.center(20, "O")
print(x)
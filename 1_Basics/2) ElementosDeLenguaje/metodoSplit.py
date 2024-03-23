#Cuando trabajas con cadenas en Python, puedes necesitar dividir una cadena en subcadenas. O puedes necesitar 
# unir fragmentos para crear una cadena. Los métodos de cadenas split() y join() te ayudan a realizar esas 
# tareas fácilmente.
#Sintaxis del método split() en Python
#Cuando necesitas dividir una cadena en subcadenas, puedes utilizar el método split().
#El método split() actúa sobre una cadena y devuelve una lista de subcadenas. 
# La sintaxis es: <cadena>.split(sep,maxsplit)
#Donde sep: es el separador que quieres usar para dividir. Debe especificarse como una cadena.
#maxsplit es un argumento opcional que indica el número de veces que quieres dividir <cadena>.
#maxsplit tiene un valor por defecto de -1, que divide la cadena en todas las apariciones de sep

print("El metodo split()")
print("----------------\n")

mi_cadena = "Yo programo dos horas al día"
#Ahora llama el método split() en mi_cadena, sin los argumentos sep ni maxsplit.
#Imprimimos la cadena modificiada
print(mi_cadena.split())

mi_cadena = "Manzanas,Naranjas,Peras,Platanos,Bayas"
print(mi_cadena.split(","))



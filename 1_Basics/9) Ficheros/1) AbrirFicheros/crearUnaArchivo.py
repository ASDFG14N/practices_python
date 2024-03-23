#"x" Create - creará un archivo, devuelve un error si el archivo existe
# "a" Agregar: creará un archivo si el archivo especificado no existe
# "w"- Escribir: creará un archivo si el archivo especificado no existe
fichero1 = open("ficheroUsa_x.txt", "x") #se crea un archivo vacio
fichero2 = open("ficheroUsa_w.txt", "w") #Crea un nuevo archivo si no existe
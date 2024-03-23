#Abre el archivo texto.txt e imprime únicamente la segunda línea.
texto = open(r"C:\Users\Gian\Desktop\ProgramPython\12) Ficheros y Excepciones\Leer y Escribir Ficheros\ejemploFicherosReadLine.txt", "r")
lineas = texto.readlines() #Lineas es una lista
lineaDos = lineas[1]
print(lineaDos)
texto.close()
fichero3 = open(r"C:\Users\Gian\Desktop\ProgramPython\12) Ficheros y Excepciones\Leer y Escribir Ficheros\ejemploFicherosReadLine.txt", "r")
una_linea = fichero3.readline()
print(una_linea) #Lee solo la primera linea
una_linea = fichero3.readline()
#Todos los metodo de los string son aplicables a las variables hechas antes de un open
print(una_linea.upper().rstrip())
una_linea = fichero3.readline()
print(una_linea.rstrip()) #no considera el alto de linea
una_linea = fichero3.readline()
print(una_linea)
una_linea = fichero3.readline()
print(una_linea)
una_linea = fichero3.readline()
print(una_linea)
una_linea = fichero3.readline()
print(una_linea)
#ESTO SUCEDE PORQUE READLINE LEE DESDE EL PUNTO ANTERIOR DONDE LOP HABIA DEJADO

"""
#Recorrer el archico linea por linea es posible:
for linea in fichero3:
    print(linea)
"""
#RECUERDA: siempre se debe cerrar los archivos.
fichero3.close()

#Si se agrega un numero como parametro este sera la cantidad de caracteres que leerá en la linea asisgnada
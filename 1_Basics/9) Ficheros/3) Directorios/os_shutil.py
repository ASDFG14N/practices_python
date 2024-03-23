import os
import shutil #Con este modulo podemos mover a otra ruta un archivo
import send2trash #con este modulo podemos enviar archivos a la papelera de reciclaje
print()
print(os.getcwd())
archivo = open("curso.txt", "w")
archivo.write("Texto de prueba")
archivo.close()
print(os.listdir())

#usando el segundo modulo
shutil.move("curso.txt", r"C:\Users\Gian\Desktop\ProgramPython\Otros Adicional") #Hemos movido el archivo

#usando el tercer modulo
send2trash.send2trash("s.txt")
#Creamos un fichero
fichero = open(r"C:\Users\Gian\Desktop\ProgramPython\12) Ficheros y Excepciones\Leer y Escribir Ficheros\ejemploFicherosWrite.txt", "w")
#Creamos una nueva variable y usmaos el metodo write()
num_car = fichero.write("Ana: 28\nJavier: 32\nEva: 45\nCarlos: 29")
print("Fichero escrito correctamente. Numero de caracteres escritos:", num_car)
#recordemos que este metodo devuelve el numero de caracteres escritos
fichero.close()
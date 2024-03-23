fichero = open(r"C:\Users\Gian\Desktop\ProgramPython\Otros Adicional\ejemplo.txt", "r")
c1 = fichero.read()
print(c1)
#Solo lectura de partes del archivo
num = fichero.read(10)
print(num) #Devolvera los 5 primers caracteres del archivo
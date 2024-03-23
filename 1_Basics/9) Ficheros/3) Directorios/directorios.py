from pathlib import Path
#Path es un objeto, no un modulo
carpeta = Path("C:/Users/Gian/Desktop/nose")
archivo = carpeta / "archo nuevo xd.txt"
mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()
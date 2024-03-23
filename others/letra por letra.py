import time

mensaje = "Hola mundo"
for letra in mensaje:
    print(letra, end="", flush=True)
    time.sleep(0.1)
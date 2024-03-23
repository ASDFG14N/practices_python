#el metodo Insert
#Sintaxis lista.insert(int(posicion), numero_elemento)
print("El metodo insert()")
print("-------------------")
print("Lista original")
letters = ["b", "d", "f", "g"]
print(f"Lista: {letters}")

print("\nInsertando 'a' en posición 0")
letters.insert(0, "a")
print(f"Lista: {letters}")

print("\nInsertando 'e' en posición 4")
letters.insert(4, "e")
print(f"Lista: {letters}")

print("\nInsertando 'z' en posición 100")
letters.insert(100, "z")
print(f"Lista: {letters}")
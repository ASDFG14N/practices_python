def invertir_lista(lista):
  new = []
  i = len(lista)
  while (i >= 0):
    if not i == len(lista):
      new.append(lista[i])
    i = i - 1
  return new



print (invertir_lista([1, 2, 3, 4]))

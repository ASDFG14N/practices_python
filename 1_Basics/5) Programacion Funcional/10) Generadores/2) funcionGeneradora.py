def funcionGenerador():
    x = 1
    yield x #1
    x += 2
    yield x #2
    x += 5
    yield x #3

g = funcionGenerador()
print(next(g)) #corresponde con el primer "yield"
print(next(g)) #corresponde con el segundo "yield"
print(next(g)) #corresponde con el tercer "yield"
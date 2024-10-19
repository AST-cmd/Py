def suma(*a):
    resultado = 0
    for numero in a:
        resultado += numero
    return resultado


c = suma(5, 6)
print(c)
d = suma(c, 6)
print(d)

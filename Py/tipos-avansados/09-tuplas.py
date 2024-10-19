hola = 5
numeros = (1, 2, 3)+(hola, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto, "+++++++++++")
menosnumeros = numeros[:2]
print(menosnumeros)

# desempaquetar tuplas
primero, segundo, *otrs = numeros
print(primero, segundo, otrs)

# iterar una tupla
for n in numeros:
    print(n)

listanumer = list(numeros)
listanumer[0] = "cerdo"
print(listanumer)

numeros = [2, 5, 6, 8, 9, 2, 6, 8, 4, 3, 6, 68, 4, 34, 6, 8466,  64, 984]

numeros.sort()
print(numeros)


numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)

usuarios = [["cerdo", 4], ["felipe", 1], ["pulga", 5]]


def ordenar(elementos):
    return elementos[1]


usuarios.sort(key=ordenar)
print(usuarios)

usuarios.sort(key=ordenar, reverse=True)
print(usuarios)

usuarios.sort(key=lambda el: el[1])
print(usuarios)

usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)

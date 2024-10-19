def sinespacios(textoe):
    textosin = ""
    for char in textoe:
        if char != " ":
            textosin += char
    textosin = list(textosin)
    textosin.sort()
    return textosin


def diccionario(textod):
    diccionari = {}
    for char in textod:
        contador = 0
        for chi in textod:
            if char == chi:
                contador += 1
        if char != diccionari:
            diccionari[char] = contador
    return diccionari


def listuplas(textotu):
    return sorted(
        textotu.items(),
        key=lambda key: key[1]
    )


while True:
    texto = input("ingresa el texto:\n>")
    if texto == "s":
        break
    textosinn = sinespacios(texto)
    diccionar = diccionario(textosinn)
    lis = listuplas(diccionar)
    print(lis)

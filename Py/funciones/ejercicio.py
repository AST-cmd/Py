print("-----------------------------------------------------------------")
print("descubre si la palabra que ingreses en un palindromo")
print("para salir solo escribe la palabra salir")
print("-----------------------------------------------------------------")


def sinespacios(texsin):
    textosin = ""
    for char in texsin:
        if char != " ":
            textosin += char
    return textosin


def es_palindromo(texto):
    texto = sinespacios(texto)
    texto2 = " "
    texto3 = " "
    for reves in reversed(texto):
        texto2 += reves
    for char in texto:
        texto3 += char
    return texto2.lower() == texto3.lower()


palabra = ""
while True:
    palabra = input("ingresa la palabra a analisar: ")
    if palabra.lower() == "salir":
        break
    else:
        print(f"la palabra: {palabra} = {es_palindromo(palabra)}")

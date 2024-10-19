def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 3)
suma(2, 5, 3, 4)
suma(2, 5, 3, 4, 7)

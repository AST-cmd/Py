numeros = list(range(1, 4))
print(numeros)

prmero, segundo, tercero = numeros
print(tercero, segundo, prmero)

prmero, *otros = numeros
print(prmero, otros)

numeros = list(range(1, 10))
prmero, segundo, *otros, ultimo = numeros
print(prmero, segundo, otros)

prmero, segundo, *otros = numeros
print(prmero, otros, ultimo)

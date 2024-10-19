# lista = [1, 2, 3, 4]
# print(*lista)

# lista2 = [5, 6]

# combinada = ["hola", *lista, "mundo", *lista2]
# print(combinada)

punto = {"x": 9, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto, "lala": "hola mundo", **punto2, "z": "mundo"}
print(nuevoPunto)

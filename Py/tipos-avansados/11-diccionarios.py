punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala")
else:
    print("lala no existe")

print(punto.get("x"))
print(punto.get("lala", 97))

del punto["x"]

del (punto["y"])
print(punto)
punto["x"] = 25
for valor in punto:
    print(valor)
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

ussuarios = [
    {"id": 1, "nombre": "Alexis"},
    {"id": 2, "nombre": "Felipe"},
    {"id": 3, "nombre": "Pepe"},
    {"id": 4, "nombre": "Pol"},
]

for usuarios in ussuarios:
    print(usuarios["nombre"])

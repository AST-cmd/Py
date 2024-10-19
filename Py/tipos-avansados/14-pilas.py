pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimo = pila.pop()
print(ultimo)
print(pila[-1])
ultimo = pila.pop()
ultimo = pila.pop()
if not pila:
    print("pila bacia ")

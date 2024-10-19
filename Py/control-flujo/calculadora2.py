print("para lasilr escribe ssalir")
print("operaciones permitidas escribe la operacion cuando te la pida")
print("suma, resta, mult, div")
numero = ""
comprobacion = True
while True:
    if not numero and comprobacion:
        numero = input("ingresa un numero: ")
        comprobacion = False
        if numero.lower() == "salir":
            break
        else:
            numero = int(numero)
    else:
        operacion = input("ingrese la operacion: ")
        if operacion.lower() == "salir":
            break

        numero2 = input("ingresa el segundo numero:")
        if numero2.lower() == "salir":
            break
        else:
            numero2 = int(numero2)

        if operacion.lower() == "suma":
            numero += numero2

        elif operacion.lower() == "resta":
            numero -= numero2

        elif operacion.lower() == "mult":
            numero *= numero2

        elif operacion.lower() == "div":
            numero /= numero2

        else:
            print("opcion no valida")
            break

        print(f"el resultado es: {numero}")

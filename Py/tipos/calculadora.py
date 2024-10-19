menu = 0
while menu != 5:
    print("Menu calculadora escoge una opcion")
    print("1-Suma")
    print("2-resta")
    print("3-Multiplicacion")
    print("4-Divicion")
    print("5-fin")
    menu = int(input("escoge una opcion: "))

    if menu == 1:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        print("---------------------------------------")
        print("Resultado: ", num1+num2)
        print("---------------------------------------")
    elif menu == 2:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        print("---------------------------------------")
        print("Resultado: ", num1-num2)
        print("---------------------------------------")
    elif menu == 3:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        print("---------------------------------------")
        print("Resultado: ", num1*num2)
        print("---------------------------------------")
    elif menu == 4:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        print("---------------------------------------")
        print("Resultado: ", num1/num2)
        print("---------------------------------------")
    else:
        print("Esa opcion no esta en el menu")

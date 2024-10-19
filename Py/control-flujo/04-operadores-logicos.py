# and, or, not
gas = False
encendido = True
edad = 18

if gas and encendido:
    print("puedes avansar   (and)")

if gas or encendido:
    print("puedes avansar  (or)")

if gas or not encendido:
    print("puedes avansar  (not)")


if gas and encendido and edad:
    print("puedes avansar   (and2)")

if gas and (encendido or edad > 17):
    print("puedes avansar   (and2)")

if not gas and (encendido or edad > 17):
    print("puedes avansar   (and2)")

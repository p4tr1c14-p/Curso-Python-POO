def calculator(txt):
    espacio1 = txt.find(" ")
    espacio2 = txt.find(" ", espacio1 + 1)

    puntos1 = txt[:espacio1]
    operador = txt[espacio1 + 1:espacio2]
    puntos2 = txt[espacio2 + 1:]

    #Contar puntos 1
    num1 = 0
    for c in puntos1:
        num1 += 1

    #Contar puntos 2
    num2 = 0
    for c in puntos2:
        num2 += 1

    #Operar según el operador
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "//":
        resultado = 0
        if num2 != 0:
            resultado = num1 // num2
    else:
        resultado = 0

    if resultado == 0:
        return ""

    res = ""
    for i in range(resultado):
        res += "."

    return res
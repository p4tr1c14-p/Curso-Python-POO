def calculate(s):
    resultado = 0
    numero = ""
    operacion = "plus"
    palabra = ""

    for letra in s:
        if letra.isdigit():
            numero += letra
        else:
            palabra += letra

            if palabra == "plus" or palabra == "minus":
                if numero:
                    if operacion == "plus":
                        resultado += int(numero)
                    else:
                        resultado -= int(numero)
                    numero = ""

                operacion = palabra  #Cambio la operación
                palabra = ""

    #Aplicao la última operación con el último número
    if numero:
        if operacion == "plus":
            resultado += int(numero)
        else:
            resultado -= int(numero)

    return str(resultado)

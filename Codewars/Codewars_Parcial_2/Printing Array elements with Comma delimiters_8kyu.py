def print_array(arr):
    resultado = ""
    contador = 0         #para saber si estoy en el último elemento

    for elemento in arr:
        #convierto el elemento a texto para poder unirlo
        texto = str(elemento)

        resultado = resultado + texto

        #si NO es el último elemento agrego una coma
        contador = contador + 1
        if contador < len(arr):
            resultado = resultado + ","

    return resultado

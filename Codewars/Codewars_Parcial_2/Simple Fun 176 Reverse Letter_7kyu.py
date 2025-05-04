def reverse_letter(st):
    result = ""  #aquí voy a guardar el resultado final

    for c in st:  #recorro cada carácter de la cadena
        if c.isalpha():  #si el carácter es una letra (no número ni símbolo)
            result = c + result  #lo agrego al inicio para ir formando la cadena invertida

    return result

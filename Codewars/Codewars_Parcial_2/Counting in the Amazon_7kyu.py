def count_arara(n):
    adak_count = n // 2  #número de pares (adak)
    anane_count = n % 2  #si no es impar, hay un "anane"

    result = ""
    for i in range(adak_count):
        if i == adak_count - 1 and anane_count == 0:
            #si es el último "adak" y no hay "anane" no agregué espacio extra

            result += "adak"
        else:
            result += "adak "

    if anane_count:
        result += "anane"

    return result

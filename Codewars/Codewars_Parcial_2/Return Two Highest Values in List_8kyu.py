def two_highest(arg1):
    #elimino los duplicados usando set y convierto a lista
    sin_duplicados = list(set(arg1))

    #y si solo hay un número o ninguno devuelvo la lista igualita
    if len(sin_duplicados) <= 1:
        return sin_duplicados

    #busco el valor más alto
    primero = max(sin_duplicados)

    #elimino ese número de la lista y buscamos el segundo más alto
    sin_duplicados.remove(primero)
    segundo = max(sin_duplicados)

    return [primero, segundo]

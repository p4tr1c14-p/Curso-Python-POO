def distinct(seq):
    #creo una lista vacía para almacenar los números sin duplicados
    resultado = []

    #recorro todos los números del ordenm original
    for num in seq:
        #si el número no está en el resultado lo agrego
        if num not in resultado:
            resultado.append(num)

    return resultado

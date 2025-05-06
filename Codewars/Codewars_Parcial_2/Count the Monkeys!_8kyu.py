def monkey_count(n):
    #creo una lista vacía donde guardé los números
    numeros = []

    i = 1
    #mientras i sea menor o igual a n sigo agregando números
    while i <= n:
        numeros.append(i)  #agrego el número i a la lista
        i = i + 1          #aumento el i en 1 para el siguiente número

    return numeros


def shift_left(a, b):
    i = len(a) - 1  #índice para a (desde el final)
    j = len(b) - 1  #índice para b (desde el final)

    #Contar el sufijo común desde el final
    while i >= 0 and j >= 0 and a[i] == b[j]:
        i -= 1
        j -= 1

    #Movimientos = letras que quedaron fuera del sufijo común en ambas cadenas
    movimientos = (i + 1) + (j + 1)
    return movimientos

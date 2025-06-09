def largest_power(N):
    if N <= 1:
        return -1  #No hay ningún 3^k menor que N

    k = 0
    valor = 1  #3^0

    while valor * 3 < N:
        valor = valor * 3
        k = k + 1

    return k
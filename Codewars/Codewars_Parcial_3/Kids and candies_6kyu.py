def candies_to_buy(amount_of_kids_invited):
    #Empiezo con 1 caramelo (mínimo común múltiplo hasta ahora)
    multiple = 1

    #Para cada número desde 1 hasta la cantidad de niños invitados
    for i in range(1, amount_of_kids_invited + 1):
        #Voy a buscar el nuevo mínimo común múltiplo entre multiple e i
        #Primero busco el máximo común divisor
        a = multiple
        b = i
        while b != 0:
            temp = b
            b = a % b
            a = temp
        gcd = a  #Aquí guardo el mcd

        #Calculo el mcd
        multiple = (multiple * i) // gcd

    return multiple

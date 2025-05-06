def remove_every_other(my_list):
    #mi lista vacía pondré los elementos que quiero conservar
    nueva_lista = []

    #recorro la lista original usando un contador
    for posicion in range(len(my_list)):
        #si la posición es par conservoo ese elemento
        if posicion % 2 == 0:
            nueva_lista.append(my_list[posicion])

    return nueva_lista

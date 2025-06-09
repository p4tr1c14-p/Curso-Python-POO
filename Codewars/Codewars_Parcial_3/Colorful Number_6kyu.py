def colorful(number):
    num_str = str(number)
    productos = []  #lista para guardar productos que ya vimos

    #Tamaño del grupo (subconjunto)
    length = 1
    while length <= len(num_str):
        start = 0
        while start <= len(num_str) - length:
            producto = 1
            i = start
            #Multiplico los dígitos en el subconjunto
            while i < start + length:
                producto = producto * int(num_str[i])
                i = i + 1

            #Verifico si producto ya está en productos
            if producto in productos:
                return False
            productos.append(producto)

            start = start + 1
        length = length + 1

    return True

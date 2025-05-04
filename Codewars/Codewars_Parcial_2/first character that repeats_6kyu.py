def first_dup(s):
    for char in s:
        if s.count(char) > 1:  #si la letra aparece más de una vez en la cadena
            return char        #devuelve la primera letra que tiene duplicados
    return None               #si no hay duplicados devuelve none
def solution(s):
    #Si la cadena tiene una cantidad impar de letras, le agregamos un guion bajo
    if len(s) % 2 != 0:
        s = s + "_"

    #Creo una lista para guardar los pares
    result = []

    #Reco la cadena de dos en dos
    i = 0
    while i < len(s):
        #Tomo dos letras y las guardamos en la lista
        pair = s[i] + s[i+1]
        result.append(pair)
        i += 2
    return result
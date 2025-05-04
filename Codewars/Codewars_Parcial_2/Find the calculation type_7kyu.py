def calc_type(a, b, res):
    suma= a + b
    resta = a - b
    multipli = a * b
    divi = a / b
    #aquí hice una comparación básica
    if suma == res:
        return "addition"
    elif resta == res:
        return "subtraction"
    elif multipli == res:
        return "multiplication"
    elif divi == res:
        return "division"
    #Esta fue la solución más simple que se me ocurrió =)
def even_or_odd(number):
    #uso el operador módulo % para verificar si el número es divisible entre 2
    if number % 2 == 0:
        return "Even"  #si el residuo es 0 el número es par
    else:
        return "Odd"   #si el residuo no es 0 el número es impar

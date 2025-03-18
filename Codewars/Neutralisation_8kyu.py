"""
Nombre: Patricia Pérez Cruz
Description:
Task 8 kyu
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
Worked Example
("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters
"""

def cadenas(signo_uno, signo_dos):
    resultado = []

    for i in signo_uno :
        for a in signo_dos:
            if signo_uno[cont] == '+' or signo_uno[i] == '-' and signo_dos[a] == '+' or signo_dos[a] == '-':
                resultado.append(i)
            else:
                resultado.append(0)
    return resultado


cad1 = input("Ingrese una: ")
cad2 = input("Ingrese otra: ")


cadenas(cad1, cad2)

#print(cadenas(["-","+", "+", "-"], ["-","+","-", "+"]))

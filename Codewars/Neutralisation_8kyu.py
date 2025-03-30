"""
Nombre: Patricia Pérez Cruz
Descripción:
Task 8 kyu
Given two strings comprised of + and -, return a new string which shows how the
two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.

("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
"""


def cadenas(signo_uno, signo_dos):
    resultado = ""  

    for i in range(len(signo_uno)):
        if signo_uno[i] == signo_dos[i]:
            resultado += signo_uno[i]  
        else:
            resultado += "0"  

    print(resultado)  #Imprimí directamente en lugar de devolver

cad1 = input("Ingrese una: ")
cad2 = input("Ingrese otra: ")

#Llamé a la función sin print, ya que dentro de la función ya la imprimí
cadenas(cad1, cad2)

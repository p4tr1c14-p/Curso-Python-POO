"""
Nombre: Patricia Pérez Cruz
Descripción:
Task 8 kyu
Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"
"""

def whatday(n):
    #Aquí hice una simple comparación y dependiendo de lo que se haya ingresado era lo que se iba a retornar
    #fue un simple ciclo de if / else
    if n == 1:
        return "Sunday"
    elif n == 2:
        return "Monday"
    elif n == 3:
        return "Tuesday"
    elif n == 4:
        return "Wednesday"
    elif n == 5:
        return "Thursday"
    elif n == 6:
        return "Friday"
    elif n == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"



"""
Nombre: Patricia Pérez Cruz
Descripción:
Task 8 kyu
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value

Examples
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
"""



def flick_switch(jsjs):
    state = True
    result = []

    for item in jsjs:
        if item == 'flick':
            state = not state
        result.append(state)

    return result


#mis pruebas
print(flick_switch(['codewars', 'flick', 'code', 'wars']))
print(flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']))
print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))

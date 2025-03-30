"""
Nombre: Patricia Pérez Cruz
Descripción:
Task 8 kyu
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
"""

def find_average(arr):
    if len(arr) == 0:
        return 0
    else:
        suma = sum(arr)
        largo = len(arr)
        total = suma / largo
# sum sumo todos los elementos en la lista arr
#Ya después saco el promedio
    return total
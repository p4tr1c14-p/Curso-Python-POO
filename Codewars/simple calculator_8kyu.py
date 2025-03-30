"""
Nombre: Patricia Pérez Cruz
Descripción:
Task 8 kyu

You are required to create a simple calculator that returns the result of addition,
subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message
"unknown value" must be returned.

Example:
arguments: 1, 2, "+"
should return 3

arguments: 1, 2, "&"
should return "unknown value"

arguments: 1, "k", "*"
should return "unknown value"

"""


def calculator(a, b, sign):
    # Esto me ayuda a verifica si ambos valores son numéricos
    #porque si 'a' y 'b' son números convertidos a cadenas me aseguro que no sean valores no numéricos

    if not (str(a).isnumeric() and str(b).isnumeric()):
        return "unknown value"

    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        return a / b
    else:
        return "unknown value"


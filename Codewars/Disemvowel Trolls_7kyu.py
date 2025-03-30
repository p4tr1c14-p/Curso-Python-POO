"""
Nombre: Patricia Pérez Cruz
Descripción:
Task 7 kyu
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel
"""

def disemvowel(string_):
    vocal = "aeiou"
    result = ""
    for i in string_:
        if i.lower() not in vocal: #Convierto lo que me den a minúscula y ya después reviso si lo que dieron es una vocal
            result = result + i
    return result

cadena = input("Ingrese su cadena a usar: ")
print(f"La cadena corregida es: {disemvowel(cadena)}")

def pluralize(word):
    largo = len(word)

    #Obtengo las últimas letras
    ultima = word[largo - 1]
    penultima = word[largo - 2] if largo >= 2 else ""

    #Reglas para "ch" y "sh"
    if penultima + ultima == "ch" or penultima + ultima == "sh":
        return word + "es"

    #Reglas para "s", "x" o "z"
    if ultima == "s" or ultima == "x" or ultima == "z":
        return word + "es"

    #Reglas para consonante + "y"
    if ultima == "y":
        if penultima != "" and penultima != "a" and penultima != "e" and penultima != "i" and penultima != "o" and penultima != "u":
            nueva = ""
            for i in range(largo - 1):
                nueva = nueva + word[i]
            return nueva + "ies"

    #En cualquier otro caso
    return word + "s"

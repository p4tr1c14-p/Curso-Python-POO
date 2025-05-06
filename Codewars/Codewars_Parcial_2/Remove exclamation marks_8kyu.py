def remove_exclamation_marks(s):
    #usaré el mé to do replace() para reemplazar todos los signos de exclamación
    #por una cadena vacía '' lo que equivale a eliminarlo
    s = s.replace('!', '')
    s = s.replace('¡', '')
    return s
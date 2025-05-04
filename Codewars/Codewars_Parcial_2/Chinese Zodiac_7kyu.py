from preloaded import animals, elements #esto ya estaba


def chinese_zodiac(year):
    #año base 1984, que es el año del "Wood Rat"
    base_year = 1984

    # calculo cuántos años han pasado desde 1984
    years_passed = year - base_year

    #encuentro el animal (cambia cada 12 años)
    animal_index = years_passed % 12
    animal = animals[animal_index]

    #encuentro el elemento (cambia cada 2 años, y hay 5 elementos)
    element_index = (years_passed // 2) % 5
    element = elements[element_index]

    return element + " " + animal

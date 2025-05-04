def age(x, y):
    # Julie = y * hermano, también Julie = hermano + x
    # Entonces: y * hermano = hermano + x
    # hermano = x / (y - 1)
    # Julie = y * hermano = y * (x / (y - 1)) = x * y / (y - 1)
    return x * y / (y - 1)

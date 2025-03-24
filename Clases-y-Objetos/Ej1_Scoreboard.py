
class Scoreboard:
    def __init__(self, points: int = 0, text_color: tuple[int]= (0, 0, 0), font : str = "kimono", size: float = 48):
        self._points = points
        self._font = font
        self._text_color = text_color
        self._size = size

    def __str__(self):
        return f"Scoreboard (point={self._points}, size= {self._size}, font= {self._font}, text_color= {self._text_color})"



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, font="Arial", text_color= (127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()
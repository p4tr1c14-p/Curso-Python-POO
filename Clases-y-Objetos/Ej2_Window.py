
from Ej1_Scoreboard import Scoreboard

class Window:
    def __init__(self, text : str, width: int, heigth: int, scoreboard: Scoreboard = Scoreboard()):
        self._text = text
        self._width = width
        self._heigth = heigth
        self._scoreboard = scoreboard


    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    @property
    def heigth(self) -> int:
        return self._heigth

    @heigth.setter
    def heigth(self, heigth: int) -> None:
        self._heigth = heigth

    @property
    def scoreboard(self) -> Scoreboard:
        return  self._scoreboard

    @scoreboard.setter
    def scoreboard(self, scoreboard: Scoreboard) -> None:
        self._scoreboard = scoreboard


    def draw_scoreboard(self) -> None:
        print(f"Score: {self._scoreboard.points}")

    def update_score(self, points : int) -> None:
        self._scoreboard.points = points
        print(f"Score: {self._scoreboard.points}") #Aquí siempre tengo que acceder con punto points porque estaba accediedo pero a
        #to_do el score y no solo a puntos

    def __str__(self):
        return f"Windows (text={self._text}, width= {self._width}, heigth= {self._heigth}, scoreboard= {self._scoreboard})"

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")
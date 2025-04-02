from Clase_Jugador import Jugador

class Equipo:
    _id = 0
    def __init__(self, nombre: str, *jugadores : Jugador):
        self._nombre = nombre
        self._id_equipo =  Equipo._id
        self._jugadores = list(jugadores)
        Equipo._id += 1

    @property  # Igual aquí con el getter obtengo valores
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter  # Y con esto asigno los datos
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property  # Igual aquí con el getter obtengo valores
    def id_equipo(self) -> int:
        return self._id_equipo

    @property  # Igual aquí con el getter obtengo valores
    def jugadores(self) -> list[Jugador]:
        return self._jugadores

    @jugadores.setter  # Y con esto asigno los datos
    def jugadores(self, jugadores: list[Jugador]) -> None:
        self._jugadores = list(jugadores)

    def agregar_jugadores(self, *jugadores: Jugador):
        for jugador in jugadores:
            self._jugadores.append(jugador)

    def remover_jugadores(self, *jugadores: Jugador):
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)

    def mostrar_jugadores(self):
        for jugador in self._jugadores:
            print(jugador)

    def total_goles(self):
        return sum(jugador.goles for jugador in self._jugadores)

    def __str__(self):
        return f"Equipo: {self._nombre}, Id: {self._id_equipo}, Total de goles: {self.total_goles()}"

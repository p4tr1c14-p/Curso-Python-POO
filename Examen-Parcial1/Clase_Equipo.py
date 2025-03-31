from Clase_Jugador import Jugador

class Equipo:
    id = 1
    def __init__(self, nombre: str, *jugadores : tuple[Jugador]):
        self._nombre = nombre
        self._id_equipo =  Equipo.id
        self._jugadores : list[Jugador]

        Equipo.id += 1
    @property  # Igual aquí con el getter obtengo valores
    def nombre(self) -> str:
        return self.nombre

    @nombre.setter  # Y con esto asigno los datos
    def nombre(self, nombre: str) -> None:
        self.nombre = nombre

    @property  # Igual aquí con el getter obtengo valores
    def id_equipo(self) -> int:
        return self.id_equipo

    @property  # Igual aquí con el getter obtengo valores
    def jugadores(self) -> tuple[Jugador]:
        return self.jugadores

    @jugadores.setter  # Y con esto asigno los datos
    def jugadores(self, jujadores: tuple[Jugador]) -> None:
        self.jugadores = jujadores


    def agregar_jugadores(self, *jugadores: tuple[Jugador]):
        pass

    def remover_jugadores(self, *jugadores: tuple[Jugador]):
        pass

    def mostrar_jugadores(self):
        pass

    def total_goles(self):
        print(f"Goles: {self.jugador.goles}")

    def __str__(self):
        #return f"
        pass

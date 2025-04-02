from Clase_Equipo import Equipo

class Jugador:
    def __init__(self, nombre: str, numero: int, goles: int = 0):
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, numero: int) -> None:
        self._numero = numero

    @property
    def goles(self) -> int:
        return self._goles

    @goles.setter
    def goles(self, goles: int) -> None:
        self._goles = goles

    def anotar_goles(self, goles = int):
        self._goles = goles

    def __str__(self):
        return f"Jugador: {self._nombre}, Número: {self._numero}, Goles: {self._goles}"

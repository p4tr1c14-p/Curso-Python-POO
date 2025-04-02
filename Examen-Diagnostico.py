"""
Patricia Pérez Cruz
04 de marzo de 2025.
Descripción del programa:

El curso tiene los siguientes equipos:

Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
Los Hackers de Café: Tania, Patricia, Rebeca.
Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
Los Ctrl+Z: Galilea, Jennifer, Juan.

Este programa debe generar 6 nuevos equipos de 2 personas cada uno,
pero con la restricción de que no puede haber dos personas que ya
estuvieron en el mismo equipo de arriba ☝️.
"""
import random

print(" GENERADOR DE EQUIPOS ")

alumnos = ["hector", "addi", "jesus alberto", "tania", "patricia", "rebeca",
           "jamileth", "bryan", "rosalinda", "galilea", "jennifer", "juan"]

anarquistas = ["hector", "addi", "jesus alberto"]
hackers = ["tania", "patricia", "rebeca"]
controlz = ["galilea", "jennifer", "juan"]
codificadores = ["jamileth", "bryan", "rosalinda"]

def generar() -> list:
    nombre_uno = random.choice(alumnos)
    nombre_dos = random.choice(alumnos)

    while nombre_uno == nombre_dos:
        nombre_dos = random.choice(alumnos)

    regresar = [nombre_uno, nombre_dos]
    return regresar

def verificar() -> list:
    while True:
        nombre_uno, nombre_dos = generar()

        if (nombre_uno in anarquistas and nombre_dos in anarquistas) or (nombre_uno in hackers and nombre_dos in hackers) or (nombre_uno in controlz and nombre_dos in controlz) or (nombre_uno in codificadores and nombre_dos in codificadores):
            print("Generando nuevos equipos porque se repiten...")
        else:
            equipo = [nombre_uno, nombre_dos]
            return equipo

def main():
    print("--")
    max = 0
    while max != 6:
        uno_equipo, dos_equipo = verificar()
        print(f"Los dos nombres son: '{uno_equipo}' y '{dos_equipo}' 🥁🥁🥁")
        max = max + 1

if __name__ == '__main__':
    main()



class Jugador:
    def __init__(self, nombre: str, numero: int, goles: int = 0):
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    @property
    def nombre(self):
        return self._nombre

    @property
    def numero(self):
        return self._numero

    @property
    def goles(self):
        return self._goles

    def anotar_goles(self, no_goles: int):
        self._goles += no_goles

    def __str__(self):
        return f"Jugador: {self._nombre}, Número: {self._numero}, Goles: {self._goles}"


class Equipo:
    _id = 0

    def __init__(self, nombre: str, *jugadores: tuple[Jugador]):
        self._id_equipo = Equipo._id
        Equipo._id += 1
        self._nombre = nombre
        self._jugadores = list(jugadores)

    @property
    def nombre(self):
        return self._nombre

    @property
    def id_equipo(self):
        return self._id_equipo

    def agregar_jugadores(self, *jugadores: tuple[Jugador]):
        self._jugadores.extend(jugadores)

    def remover_jugadores(self, *jugadores: tuple[Jugador]):
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)

    def mostrar_jugadores(self):
        for jugador in self._jugadores:
            print(jugador)

    def total_goles(self):
        return sum(jugador.goles for jugador in self._jugadores)

    def __str__(self):
        return f"Equipo: {self._nombre}, ID: {self._id_equipo}, Total Goles: {self.total_goles()}"


class Torneo:
    def __init__(self, nombre: str, *equipos: tuple[Equipo]):
        self._nombre = nombre
        self._equipos = list(equipos)

    @property
    def nombre(self):
        return self._nombre

    def agregar_equipos(self, *equipos: tuple[Equipo]):
        self._equipos.extend(equipos)

    def remover_equipos(self, *equipos: tuple[Equipo]):
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)

    def mostrar_equipos(self):
        for equipo in self._equipos:
            print(equipo)

    def generar_rol(self):
        # Implementar lógica para generar rol de juegos
        pass

    def __str__(self):
        return f"Torneo: {self._nombre}, Equipos: {len(self._equipos)}"

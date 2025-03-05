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

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

alumnos = ["hector", "addi", "jesus alberto","tania", "patricia", "rebeca",
           "jamileth", "bryan", "rosalinda", "galilea", "jennifer", "juan" ]

anarquistas = ["hector", "addi", "jesus alberto"]
hackers = ["tania", "patricia", "rebeca"]
controlz = ["galilea", "jennifer", "juan"]
codificadores = ["jamileth", "bryan", "rosalinda"]

def generar() -> list:
    mi_lista = []

    nombre_uno = random.choice(alumnos)
    nombre_dos = random.choice(alumnos)
    mi_lista = [nombre_uno, nombre_dos]

    return mi_lista

def verificar() -> list:
    bandera = True
    nombre_uno, nombre_dos = generar()

    while bandera:
        if nombre_uno and nombre_dos in anarquistas:
            print("Generando nuevos equipos porque se repiten...")
            name_uno, name_dos = generar()
            final = [name_uno, name_dos]
            bandera = False
            return final

        if nombre_uno and nombre_dos in hackers:
            print("Generando nuevos equipos porque se repiten...")
            name_uno, name_dos = generar()
            final = [name_uno, name_dos]
            bandera = False
            return final

        if nombre_uno and nombre_dos in controlz:
            print("Generando nuevos equipos porque se repiten...")
            name_uno, name_dos = generar()
            final = [name_uno, name_dos]
            bandera = False
            return final

        if nombre_uno and nombre_dos in codificadores:
            print("Generando nuevos equipos porque se repiten...")
            name_uno, name_dos = generar()
            final = [name_uno, name_dos]
            bandera = False
            return final

def main():
    print("--")
    max = 0
    while max != 6:
        verificar()
        uno_equipo, dos_equipo = generar()
        print(f"Los dos nombres son: '{uno_equipo}' y '{dos_equipo}' 🥁🥁🥁")
        max = max + 1

if __name__ == '__main__':
     main()
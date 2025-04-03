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

"""from Clase_Jugador import Jugador
from Clase_Equipo import Equipo
from Clase_Torneo import Torneo"""
"""
torneo = Torneo("Champions League")


print("-- Bienvenido al torneo: Champions League.  --\n")
print("1. Crear nuevo jugador.")
print("2. Crear nuevo equipo.")
print("3. Ver lista de jugadores.")
print("4. Ver lista de equipos.")
print("5. Agregar jugadores a algún equipo.")
print("6. Eliminar jugadores de un equipo.")
print("7. Agregar equipos al torneo.")
print("8. Eliminar equipos del torneo.")
print("9. Anotar gol(es) a un jugador.")
print("10. Conocer el número total de goles de los equipos.")
print("11. Generar rol de juegos.")
print("0. Salir.\n")
opcion = int(input("Por favor, ingresa una de las opciones anteriores:"))
#validar si lo que me den sea numero valido o no cadena


while opcion != 0:
    if opcion == 0:
        print("Gracias =)")
    elif opcion == 1:
        #Jugador
        lista_jugadores = Equipo["Lista jugadores"]
        nombre = input("Ingresa el nombre del jugador: ")
        numero = int(input("Ingresa el número: "))
        goles = int(input("Ingresa el número de goles: "))
        while bool(nombre) and bool(numero) and bool(goles):
            #validar
            jugador1 = Jugador(nombre, numero, goles)
            lista_jugadores.agregar_jugadores(jugador1)

        nombre = input("Ingresa el nombre del jugador: ")
        numero = int(input("Ingresa el numero: "))
        goles = int(input("Ingresa el número de goles: "))

    elif opcion == 2:
        #Equipo
        lista_equipo = Torneo["Lista equipo"]
        equipo_nombre = input("Ingresa el nombre del equipo o enter para terminar: ")

        while bool(equipo_nombre):
            mi_equipo = Equipo(mi_equipo)
            lista_equipo.agregar_equipos(mi_equipo)

        equipo_nombre = input("Ingresa el nombre del equipo o enter para terminar: ")

    elif opcion == 3:
        #Ver lista de equpos"""
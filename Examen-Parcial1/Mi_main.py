from Clase_Jugador import Jugador
from Clase_Equipo import Equipo
from Clase_Torneo import Torneo

# Creamos el torneo
torneo = Torneo("Champions League")

# Listas para almacenar jugadores que no están asignados a equipos
jugadores_sin_equipo = []


def validar_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():  # Verifica si la entrada es un número positivo
            return int(valor)
        else:
            print("Error: Por favor ingresa un número válido.")


def mostrar_menu():
    print("\n-- Bienvenido al torneo: Champions League.  --\n")
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


def main():
    while True:
        mostrar_menu()
        opcion = validar_entero("Por favor, ingresa una de las opciones anteriores: ")

        if opcion == 0:
            print("Gracias por usar el sistema =)")
            break

        elif opcion == 1:
            # Crear nuevo jugador
            print("\n-- Crear nuevo jugador --")
            nombre = input("Ingresa el nombre del jugador (o enter para cancelar): ")

            if nombre:
                numero = validar_entero("Ingresa el número: ")
                goles = validar_entero("Ingresa el número de goles: ")
                nuevo_jugador = Jugador(nombre, numero, goles)
                jugadores_sin_equipo.append(nuevo_jugador)
                print(f"Jugador {nombre} creado con éxito.")

        elif opcion == 2:
            # Crear nuevo equipo
            print("\n-- Crear nuevo equipo --")
            nombre_equipo = input("Ingresa el nombre del equipo (o enter para cancelar): ")

            if nombre_equipo:
                nuevo_equipo = Equipo(nombre_equipo)
                agregar_jugadores_al_crear = input("¿Deseas agregar jugadores al equipo? (s/n): ").lower()

                if agregar_jugadores_al_crear == 's':
                    # Mostrar jugadores disponibles
                    if jugadores_sin_equipo:
                        print("\nJugadores disponibles:")
                        for i, jugador in enumerate(jugadores_sin_equipo):
                            print(f"{i + 1}. {jugador}")

                        while True:
                            seleccion = input("\nIngresa el número del jugador a agregar (o enter para terminar): ")
                            if not seleccion:
                                break

                            if seleccion.isdigit():  #verifica si la entrada es un número positivo
                                indice = int(seleccion) - 1
                                if 0 <= indice < len(jugadores_sin_equipo):
                                    nuevo_equipo.agregar_jugadores(jugadores_sin_equipo[indice])
                                    print(f"Jugador {jugadores_sin_equipo[indice].nombre} agregado al equipo.")
                                    jugadores_sin_equipo.pop(indice)
                                else:
                                    print("Número de jugador inválido")
                            else:
                                print("Por favor ingresa un número válido")

                print(f"Equipo {nombre_equipo} creado con éxito 🤠")
                torneo.agregar_equipos(nuevo_equipo)

        elif opcion == 3:
            #ver mi lista de jugadores
            print("\n-- Lista de jugadores --")
            if jugadores_sin_equipo:
                print("\nJugadores sin equipo:")
                for jugador in jugadores_sin_equipo:
                    print(jugador)

            print("\nJugadores en equipos:")
            for equipo in torneo._equipos:
                print(f"\nEquipo: {equipo.nombre}")
                equipo.mostrar_jugadores()

            if not jugadores_sin_equipo and not torneo._equipos:
                print("No hay jugadores registrados.")

        elif opcion == 4:
            #ver la lista de mis equiposs
            print("\n-- Lista de equipos --")
            if torneo._equipos:
                torneo.mostrar_equipos()
            else:
                print("No hay equipos registrados en el torneo 🤡")

        elif opcion == 5:
            #agregar jugadores a algún equipo
            print("\n-- Agregar jugadores a equipo --")
            if not torneo._equipos:
                print("No hay equipos registrados primero debes crear un equipo y ya después puedes escoger a los jugadores que quieras")
                continue

            if not jugadores_sin_equipo:
                print("No hay jugadores disponibles para agregar. Primero crea algunos jugadores.")
                continue

            print("\nEquipos disponibles:")
            for i, equipo in enumerate(torneo._equipos): #enumerate para que tenga numeración ya que obtiene el índice
                print(f"{i + 1}. {equipo.nombre}")

            indice_equipo = validar_entero("\nSelecciona el número del equipo: ") - 1 #-1 para no tener un desborde
            if 0 <= indice_equipo < len(torneo._equipos): #verifico si el índice del equipo está dentro del rango válido de equipos en el torneo
                equipo_seleccionado = torneo._equipos[indice_equipo]

                print("\nJugadores disponibles:")
                for i, jugador in enumerate(jugadores_sin_equipo):
                    print(f"{i + 1}. {jugador}")

                while True:
                    seleccion = input("\nIngresa el número del jugador a agregar (o enter para terminar): ")
                    if not seleccion:
                        break

                    if seleccion.isdigit():  #verificou si la entrada es un número positivo
                        indice = int(seleccion) - 1
                        if 0 <= indice < len(jugadores_sin_equipo):
                            equipo_seleccionado.agregar_jugadores(jugadores_sin_equipo[indice])
                            print(
                                f"Jugador {jugadores_sin_equipo[indice].nombre} agregado al equipo {equipo_seleccionado.nombre}")
                            jugadores_sin_equipo.pop(indice)
                        else:
                            print("Número de jugador inválido")
            else:
                print("Número de equipo inválido")

        elif opcion == 6:
            #eliminar jugadores de un equipo
            print("\n-- Eliminar jugadores de un equipo --")
            if not torneo._equipos:
                print("No hay equipos registrados.")
                continue

            print("\nEquipos disponibles:")
            for i, equipo in enumerate(torneo._equipos):
                print(f"{i + 1}. {equipo.nombre}")

            indice_equipo = validar_entero("\nSelecciona el número del equipo: ") - 1
            if 0 <= indice_equipo < len(torneo._equipos):
                equipo_seleccionado = torneo._equipos[indice_equipo]

                if not equipo_seleccionado.jugadores:
                    print(f"El equipo {equipo_seleccionado.nombre} no tiene jugadores")
                    continue

                print("\nJugadores del equipo:")
                for i, jugador in enumerate(equipo_seleccionado.jugadores):
                    print(f"{i + 1}. {jugador}")

                while True:
                    seleccion = input("\nIngresa el número del jugador a eliminar (o enter para terminar): ")
                    if not seleccion:
                        break

                    if seleccion.isdigit():  # verifico si la entrada es un número positivo
                        indice = int(seleccion) - 1
                        if 0 <= indice < len(equipo_seleccionado.jugadores):
                            jugador_eliminado = equipo_seleccionado.jugadores[indice]
                            equipo_seleccionado.remover_jugadores(jugador_eliminado)
                            jugadores_sin_equipo.append(jugador_eliminado)
                            print(
                                f"Jugador {jugador_eliminado.nombre} eliminado del equipo y añadido a jugadores disponibles")
                        else:
                            print("Número de jugador inválido")
                    else:
                        print("Por favor ingresa un número válido")

        elif opcion == 7:
            #agregar equipos al torneo
            print("\n-- Agregar equipos al torneo --")
            nombre_equipo = input("Ingresa el nombre del nuevo equipo (o enter para cancelar): ")

            if nombre_equipo:
                nuevo_equipo = Equipo(nombre_equipo)
                torneo.agregar_equipos(nuevo_equipo)
                print(f"Equipo {nombre_equipo} agregado al torneo")

        elif opcion == 8:
            #eliminar equipos del torneo
            print("\n-- Eliminar equipos del torneo --")
            if not torneo._equipos:
                print("No hay equipos registrados en el torneo")
                continue

            print("\nEquipos en el torneo:")
            for i, equipo in enumerate(torneo._equipos):
                print(f"{i + 1}. {equipo.nombre}")

            indice_equipo = validar_entero("\nSelecciona el número del equipo a eliminar: ") - 1
            if 0 <= indice_equipo < len(torneo._equipos):
                equipo_eliminado = torneo._equipos[indice_equipo]

                #recuperar jugadores del equipo eliminado
                for jugador in equipo_eliminado.jugadores:
                    jugadores_sin_equipo.append(jugador)

                torneo.remover_equipos(equipo_eliminado)
                print(f"Equipo {equipo_eliminado.nombre} eliminado del torneo")
                print("Los jugadores del equipo han sido añadidos a la lista de jugadores disponibles")
            else:
                print("Número de equipo inválido")

        elif opcion == 9:
            #anotar gol / es a un jugador
            print("\n-- Anotar goles a un jugador --")

            #buscar todos los jugadores (en equipos y disponibles)
            todos_jugadores = jugadores_sin_equipo.copy()
            for equipo in torneo._equipos:
                todos_jugadores.extend(equipo.jugadores)

            if not todos_jugadores:
                print("No hay jugadores registrados")
                continue

            print("\nJugadores disponibles:")
            for i, jugador in enumerate(todos_jugadores):
                print(f"{i + 1}. {jugador}")

            indice_jugador = validar_entero("\nSelecciona el número del jugador: ") - 1
            if 0 <= indice_jugador < len(todos_jugadores):
                jugador_seleccionado = todos_jugadores[indice_jugador]
                goles_anotados = validar_entero("Ingresa el número de goles a añadir: ")

                jugador_seleccionado.anotar_goles(goles_anotados)
                print(f"Se han anotado {goles_anotados} goles a {jugador_seleccionado.nombre}.")
                print(f"Total de goles: {jugador_seleccionado.goles}")
            else:
                print("Número de jugador inválido")

        elif opcion == 10:
            #conocer el número total de goles de los equipos
            print("\n-- Total de goles por equipo --")
            if not torneo._equipos:
                print("No hay equipos registrados en el torneo")
                continue

            total_general = 0
            for equipo in torneo._equipos:
                total_equipo = equipo.total_goles()
                print(f"Equipo {equipo.nombre}: {total_equipo} goles")
                total_general += total_equipo

            print(f"\nTotal general de goles en el torneo: {total_general}")

        elif opcion == 11:
            #generar rol de juegos
            print("\n-- Generar rol de juegos --")
            torneo.generar_rol()

        else:
            print("Opción inválida. Por favor intenta de nuevo.")

        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()
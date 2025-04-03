from Clase_Equipo import Equipo

class Torneo:
    def __init__(self, nombre: str, *equipos: tuple[Equipo]):
        self._nombre = nombre
        self._equipos = list(equipos)

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

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
        """
        Genera un calendario de partidos 'todos contra todos'.
        Si hay un número impar de equipos, se añade un equipo ficticio llamado "Descanso".
        """
        if len(self._equipos) < 2:
            print("No hay suficientes equipos para generar un torneo.")
            return

        # Hacer una copia de los equipos manualmente para no modificar la lista original
        equipos = []
        for equipo in self._equipos:
            equipos.append(equipo)

        # Si hay un número impar de equipos, añadimos un equipo ficticio llamado "Descanso"
        if len(equipos) % 2 != 0:
            descanso = Equipo("Descanso")
            equipos.append(descanso)
            print("Nota: Se ha añadido un equipo 'Descanso' para completar el calendario.")

        num_equipos = len(equipos)
        num_jornadas = num_equipos - 1

        print("\nCalendario de partidos:")

        for jornada in range(num_jornadas):
            print(f"\nJornada {jornada + 1}:")

            partidos = []
            for i in range(num_equipos // 2):
                equipo_local = equipos[i]
                equipo_visitante = equipos[num_equipos - 1 - i]  # Último equipo

                if equipo_local.nombre == "Descanso":
                    print(f"El equipo {equipo_visitante.nombre} descansa esta jornada.")
                elif equipo_visitante.nombre == "Descanso":
                    print(f"El equipo {equipo_local.nombre} descansa esta jornada.")
                else:
                    print(f"{equipo_local.nombre} vs {equipo_visitante.nombre}")
                    partidos.append([equipo_local, equipo_visitante])

            # Rotación de equipos
            if num_jornadas > 1:
                primer_equipo = equipos[0]
                ultimo_equipo = equipos[-1]
                equipos = [primer_equipo] + [ultimo_equipo] + equipos[1:num_equipos - 1]
                #selecciono los equipos intermedios (sin el primero ni el último) para rotarlos
    def __str__(self):
        return f"Torneo: {self._nombre}, Equipos: {len(self._equipos)}"
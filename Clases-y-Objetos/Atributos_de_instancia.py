class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_tema(self, tema: str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")


class Profesor:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.temas_dominados = []

    def dominar_tema(self, tema: str):
        self.temas_dominados.append(tema)
        print(f"{self.nombre} domina el tema {tema}")

    def ensenar_tema(self, no_tema: int) -> str:
        if 0 <= no_tema < len(self.temas_dominados):
            tema = self.temas_dominados[no_tema]
            print(f"{self.nombre} enseñará el tema {tema}")
            return tema
        else:
            print(f"Error: El profesor {self.nombre} no tiene un tema con el índice {no_tema}")


if __name__ == "__main__":
    nombre_profesor = input("Ingrese el nombre del profesor: ")
    profesor = Profesor(nombre_profesor)

    print("\nIngrese los temas que domina el profesor (escriba 'fin' para terminar):")
    while True:
        tema = input("Tema: ")
        if tema.lower() == 'fin':
            break
        profesor.dominar_tema(tema)

    print("\nTemas dominados por el profesor:")
    for i, tema in enumerate(profesor.temas_dominados):
        print(f"{i}: {tema}")

    nombre_estudiante = input("\nIngrese el nombre del estudiante: ")
    estudiante = Estudiante(nombre_estudiante)

    print("Selección de temas para enseñar:")
    while True:
        indice_str = input("\nIngrese el índice del tema a enseñar (o 'fin' para terminar): ")

        if indice_str.lower() == 'fin':
            break

        indice = int(indice_str)
        tema = profesor.ensenar_tema(indice)
        estudiante.aprender_tema(tema)


    print(f"Temas aprendidos por {estudiante.nombre}:")
    if estudiante.temas_aprendidos:
        for tema in estudiante.temas_aprendidos:
            print(f"- {tema}")
    else:
        print("El estudiante no ha aprendido ningún temaa")
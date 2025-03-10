class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_tema(self, tema: str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

    def __str__(self) -> str:
        return f"Estudiante (nombre: {self.nombre}, temas_aprendidos: {self.temas_aprendidos})"


class Profesor:
    def __init__(self, nombre: str, temas_dominados: list[str]):
        self.nombre = nombre
        self.temas_dominados = []



    def dominar_tema(self, tema: str):
        self.temas_dominados.append(tema)
        print(f"{self.nombre} domina el tema {tema}")

    def ensenar_tema(self, no_tema: int) -> str:
        if no_tema > len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"



    def __str__(self) -> str:
        return f"Estudiante (nombre: {self.nombre}, temas_aprendidos: {self.temas_dominados})"



if __name__ == "__main__":

    estudiante1 = Estudiante("Loopy")
    estudiante2 = Estudiante("Lusi")

    profesor1 = Profesor("Alberto")

    estudiante1.aprender_tema("Evolución sitios web")
    estudiante2.aprender_tema("IoT")

    profesor1.temas_dominados = ("Paradigmas de programación")

    print(estudiante1)
    print(estudiante2)

    print(profesor1)
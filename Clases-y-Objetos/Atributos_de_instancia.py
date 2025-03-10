

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
        self.temas_dominados = temas_dominados



    def dominar_tema(self, tema: str):
        self.temas_dominados.append(tema)
        print(f"{self.nombre} domina el tema {tema}")

    def ensenar_tema(self, no_tema: int) -> str:
        if 0 <= no_tema < len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"


    def __str__(self) -> str:
        return f"Profesor (nombre: {self.nombre}, temas_aprendidos: {self.temas_dominados})"



if __name__ == "__main__":

    estudiante1 = Estudiante("Loopy")
    estudiante2 = Estudiante("Lusi")


    profesor1 = Profesor("Alberto", ["Paradigmas de programación", "Matemáticas"])

    estudiante1.aprender_tema("Evolución sitios web")
    estudiante2.aprender_tema("IoT")

    profesor1.dominar_tema("Base")

    indice = input("Ingresa un subíndice: ")
    if indice.isnumeric():
        enviar = int(indice)
        tema = profesor1.ensenar_tema(enviar)
        print(tema)
    else:
        print("Valor no válido")



    print(estudiante1)
    print(estudiante2)

    print(profesor1)

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
        print(f"{self.nombre} domina los temas {tema}")

    def ensenar_tema(self, no_tema: int) -> str:
        #Correjir
        self.ensenar_tema.append(no_tema)
        print(f"{self.nombre} enseñará los temas {no_tema}")
        return no_tema


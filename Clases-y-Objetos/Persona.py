

class Persona:
    def __init__(self, nombre:str,edad:int,
                 altura:float, peso:float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def caminar(self) -> None:
        print("Estoy caminando 🚶‍♂️‍➡️")

    def comer(self) -> None:
        print("Estoy comiendo 🥞")

    def jugar(self) -> None:
        print("Estoy jugando ️‍🛝")

    def dormir(self) -> None:
        print("Estoy durmiendo 😴")

if __name__ == '__main__':
        patricia = Persona("Patricia Pérez Cruz", 19,
                           1.59, 69.0)

        print(patricia.nombre)
        print(patricia.edad)
        print(patricia.altura)
        print(patricia.peso)

        patricia.caminar()
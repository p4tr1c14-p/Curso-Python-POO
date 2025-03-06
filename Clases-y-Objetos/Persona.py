

class Persona:
    def __init__(self, nombre:str,edad:int,
                 altura:float, peso:float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def caminar(self) -> None:
        print(f"{self.nombre} esta caminando 🚶‍♂️‍➡️"
              f"para bajar sus {self.peso}kg")

    def comer(self) -> None:
        print("Estoy comiendo 🥞")

    def jugar(self) -> None:
        print("Estoy jugando ️‍🛝")

    def dormir(self) -> None:
        print("Estoy durmiendo 😴")

if __name__ == '__main__':
        patricia = Persona("Patricia Pérez Cruz", 21,
                           1.59, 60.0)

        lusi = Persona("Zhao Lusi", edad= 25,
                       altura= 1.59, peso= 50.0)

        lusi.caminar()
        lusi.comer()

        patricia.peso = 40.0
        patricia.edad = 19
        patricia.caminar()
        print(f"Mi nombre es: {patricia.nombre}")



        """print(patricia.nombre)
        print(patricia.edad)
        print(patricia.altura)
        print(patricia.peso)

        patricia.caminar()
        """


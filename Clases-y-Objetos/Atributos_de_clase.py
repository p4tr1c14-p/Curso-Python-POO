class Empleado:
    no_id = 1
    def __init__(self, nombre : str, sueldo: float):
        self.nombre = nombre
        self.sueldo = sueldo

        self.no_id = Empleado.no_id
        Empleado.no_id += 1

    def __str__(self) -> str:
        return f"Empleado (id: {self.no_id}, nombre: {self.nombre}, sueldo: {self.sueldo})"

    def aumentar_sueldo(self, porcentaje: float) -> None:
        pass


if __name__ == '__main__':
    print(Empleado.no_id)

    empleado1 = Empleado("Hola", 200.0)
    empleado2 = Empleado("María", 500.0)

    print(empleado1)
    print(empleado2)

    print(Empleado.no_id)

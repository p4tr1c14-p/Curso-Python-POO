class Empleado:
    no_id = 1
    def __init__(self, nombre : str, sueldo: float):
        self.nombre = nombre
        self.sueldo = sueldo

        self.no_id = Empleado.no_id
        Empleado.no_id += 1

    def aumentar_sueldo(self, porcentaje: float) -> None:
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        if porcentaje > 0:
            self.sueldo += self.sueldo * (porcentaje / 100)
            print(f"El sueldo de {self.nombre} ahora es de {self.sueldo:,.2f}")

        else:
            print("No se aplicó ningún cambio, ya que por Ley, el sueldo no puede disminuir.")

    def __str__(self) -> str:
        return f"Empleado(id: {self.no_id}, Nombre: {self.nombre}, Sueldo: {self.sueldo:,.2f})"

class Empresa:
    def __init__(self, nombre : str, *empleados: Empleado):
        self.nombre = nombre
        self.empleados = list(empleados)

    def agregar_empleados(self, *nuevos_empleados: Empleado):
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def mostrar_empleados(self) -> None:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        print(f"*** Lista de empleados de {self.nombre} ***")

        for empleado in self.empleados:
            print(empleado)

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del metodo str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"

if __name__ == '__main__':
    sofia = Empleado("Sofi", 120)
    lusi = Empleado("Lusi", 1000)
    print(lusi)
    unsij = Empresa("UNSIJ")
    unsij.agregar_empleados(lusi, sofia)

    lusi.nombre = "Zhao Lusi"
    print(unsij)
    print(sofia)
    print(lusi)

    print(lusi.nombre )
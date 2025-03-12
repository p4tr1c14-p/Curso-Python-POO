"""
Nombre: Patricia Pérez Cruz
Fecha:
Descripción:
Ejemplo de uso de los atributos de clase.

Los atributos de clase son variables que pertenecen a la clase en sí, no a las instancias (objetos) de la clase.
Esto significa que todos los objetos comparten el mismo valor para estos atributos.
Úsalos para valores constantes, contadores, configuraciones globales o cualquier dato que deba ser compartido
entre todas las instancias de la clase.

"""

""" %%%%%%%     Clase    %%%%%%%%%%%%%%%%%%%%% """
class Personaje:
    """
    Clase que representa a un empleado.
    Sus atributos son: no_id (atributo de clase), nombre y sueldo.
    Sus métodos son: __init__(), __str__(), aumentar_sueldo().
    """

    # Atributo de clase. En este caso, se utiliza para generar ID de los empleados.
    contador_id = 1

    def __init__(self, x: int, y: int):
        """
        Constructor de mi personaje.
        :param x: X.
        :param y: y.
        """

        # Atributos de instancia.
        self.x = x
        self.y = y

        # Se asigna el atributo de clase como atributo de instancia y luego se incrementa.
        # Nota: Para utilizar los atributos de clase, se utiliza el nombre de la clase seguido de un punto
        # y el nombre del atributo.
        self.id = Personaje.contador_id
        Personaje.contador_id += 1


    def moverse(self, ordenes: str) -> None:
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param ordenes: Se usa para saber qué hacer.
        """
        pass

    def posicion_actual(self, x: int, y: int) -> None:
        pass

    def __str__(self) -> str:
        """
        Se utiliza para definir la representación en cadena de mi personaje.
        :return: El objeto en forma de cadena.
        """
        return f"Empleado(id: {self.contador_id}, Posición x: {self.x}, Posición y: {self.y})"



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Ejemplo de uso de los atributos de clase.
    print("  -- Ejemplo de uso de los atributos de clase.")

    # Forma de acceder al atributo de clase.
    print(f"Personaje (id: {Personaje.contador_id }, x: {Personaje(x=)}, y: {Personaje(y=)})")


    # Se crean varios objetos de mi clase Personaje y se imprimen en consola.
    mi_personaje = Personaje(0, 0)
    dos = Personaje(9, 8)


    print()
    print("Se crea mi personaje 😎:")
    print(mi_personaje)

    # Se muestra nuevamente el atributo de clase.
    print()
    print(f"Atributo de clase: {Personaje.contador_id = }")
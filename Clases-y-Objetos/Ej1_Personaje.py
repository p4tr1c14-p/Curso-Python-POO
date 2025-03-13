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

    def __init__(self):
        """
        Constructor de mi personaje.
        :param x: X.
        :param y: y.
        """

        # Atributos de instancia.
        self.x = 0
        self.y = 0

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
        for orden in ordenes:
            if orden in ['A', 'a'] and self.y < 10:
                self.y += 1
            elif orden in ['R', 'r'] and self.y > 0:
                self.y -= 1
            elif orden in ['D', 'd'] and self.x < 10:
                self.x += 1
            elif orden in ['I', 'i'] and self.x > 0:
                self.x -= 1

    def posicion_actual(self) -> None:
        print(f"Personaje {self.id} en posición: ({self.x}, {self.y})")

    def __str__(self) -> str:
        """
        Se utiliza para definir la representación en cadena de mi personaje.
        :return: El objeto en forma de cadena.
        """
        return f"Personaje {self.id} en ({self.x}, {self.y})"


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Crear un personaje
    personaje = Personaje()
    print("Personaje creado en el origen (0, 0)")
    print("Movimientos válidos: A (avanzar y), R (retroceder y), D (derecha x), I (izquierda x)")
    print("Ingrese 'S' para salir")

    while True:
        secuencia = input("Ingresa tus movimientos: ")
        movimiento = secuencia.lower()
        if 'S' in secuencia or 's' in secuencia:
            print("Fin del programa")
            break
        elif movimiento.isnumeric():
            print("Ingrese un valor válido porfii")
            print("Movimientos válidos: A (avanzar y), R (retroceder y), D (derecha x), I (izquierda x) \n")

        # Realizar movimientos
        personaje.moverse(secuencia)

        # Mostrar posición final
        personaje.posicion_actual()

class Vehiculo:

    def init(self, velocidad_maxima: int, kilometraje: int):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje


class Punto:

    def punto(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


    def mostrar(self):
        print(f"X en {self.x} Y en {self.y}")


    def mover(self, punto1: float, punto2: float):
        self.x = punto1
        self.y = punto2


    def calcular_distancia(self):


class Rectangulo:

    def init(self, esquina1: float, esquina2: float):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def perimetro(self):

    def area(self):

    def es_cuadrado(self):
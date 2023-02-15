#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
import math


class Vehiculo:

    def init(self, velocidad_maxima: int, kilometraje: int):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

#Cree una clase Punto que represente un punto en el plano cartesiano.
class Punto:

    def punto(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

#Un método mostrar que imprima por consola las coordenadas del punto
    def mostrar(self):
        print(f"X en {self.x} Y en {self.y}")

#Un método mover que cambie las coordenadas del punto
    def mover(self, p1: float, p2: float,p3: float, p4: float):
        self.x = p1 + 2
        self.y = p2 + 5
        self.x1 = p3 + 7
        self.y1 = p4 + 4


#Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
    def calcular_distancia(self):

        distanciax = self.x - self.x1
        distanciay = self.y - self.y1

        return distanciax, distanciay



#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los
# puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro,
# calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:

    def __int__(self, esquina1: float, esquina2: float):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def perimetro_r(self,x: int, y: int,x3: int, y3: int):
        self.x = x
        self.y = y
        self.x3 = x3
        self.y3 = y3

        suma_perimetro = x + y + x3 + y3

        return suma_perimetro



    def area_r(self, x1: int, y1: int,x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        base = x1 + x2
        altura = y1 + y2

        area = base * altura

        return area



    def es_cuadrado(self):

        b = self.x - self.x1
        a = self.y - self.y1

        if (b == a):
            print ("es un cuadrado")

        else:
            print ("no es un cuadrado")


#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el
# constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

class Circulo:
    def __int__(self, centro: int, radio: int):
        self.centro = centro
        self.radio = radio

    def area_c (self):
        area = math.pi(self.radio*self.centro)
        return area

    def perimetro_c (self):

        perimetro_c = 2*math.pi * self.radio
        return perimetro_c

#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción
#del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:
     def __int__(self, valor: int, pinta: int):
         self.valor = valor
         self.pinta = pinta

#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben
# inicializar en el constructor con valores recibidos como parámetros.

class CuentaBancaria:
    def __int__(self,numero_cuenta: int,propietarios: int,balance: int):
        self.numero_cuenta =numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar (self)

    def retirar (self)

    def plicar_cuota_manejo (self)

    def mostrar_detalles (self)
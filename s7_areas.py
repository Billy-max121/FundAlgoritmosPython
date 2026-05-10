from math import pow, pi

class Areas:

    def area_cuadrado(self, lado):
        return lado * lado

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def area_circulo(self, radio):
        return pi * pow(radio, 2)


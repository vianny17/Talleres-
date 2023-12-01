class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

class Circulo(Forma):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def calcular_circunferencia(self):
        return self.ancho * self.alto

Circulo = Circulo(ancho=18, alto=40)

circunferencia = Circulo.calcular_circunferencia()
print(f"El área de la forma es: {circunferencia}")
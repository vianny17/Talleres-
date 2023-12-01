class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

Forma = Forma(ancho=4, alto=18)

area = Forma.calcular_area()
print(f"El área de la forma es: {area}")
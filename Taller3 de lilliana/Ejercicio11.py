class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def calcular_perimetro(self):
        return self.ancho * self.alto

Rectangulo = Rectangulo(ancho=10, alto=20)

perimetro = Rectangulo.calcular_perimetro()
print(f"El perimetro de la forma es: {perimetro}")
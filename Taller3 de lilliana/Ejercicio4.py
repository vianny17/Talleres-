class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_ruido(self):
        print (f"Nombre: {self.nombre}, Edad: {self.edad}, Este es un mensaje genérico.")

mi_animal = Animal("Berlin", 2)

mi_animal.hacer_ruido()
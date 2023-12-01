class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_ruido(self):
        print (f"Nombre: {self.nombre}, Edad: {self.edad}, Este es un mensaje genérico.")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    def hacer_ruido(self):
        print(f"{self.nombre} ladra guau, guau") 

Perro = Perro(nombre="Berlin", edad=2, raza="Pequeñez")
Perro.hacer_ruido()
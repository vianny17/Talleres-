class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_ruido(self):
        print (f"Nombre: {self.nombre}, Edad: {self.edad}, Este es un mensaje genérico.")

class Gato(Animal):
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        self.pelaje = pelaje
    def hacer_ruido(self):
        print(f"{self.nombre} Maulla miau, miau") 

Gato = Gato(nombre="Ágata", edad=1, pelaje="Atigrado")
Gato.hacer_ruido()
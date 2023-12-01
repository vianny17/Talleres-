class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas
    def obtener_info(self):
        super().obtener_info()
        print(f"Número de puertas: {self.numero_puertas}")

automovil = Automovil("Toyota", "Mustang", 4)
automovil.obtener_info()

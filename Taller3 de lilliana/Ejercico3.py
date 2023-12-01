class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
    
class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga
    def obtener_info(self):
        super().obtener_info()
        print(f"Capacidad de carga: {self.capacidad_carga}")

Camioneta = Camioneta("Ford", "Focus", 80)
Camioneta.obtener_info()
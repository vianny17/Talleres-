class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
    def obtener_info(self):
        return f"marca: {self.marca}: modelo: {self.modelo}, año: {self.año}"

Vehiculo1 = Vehiculo("Toyota", "public", 2020)
Vehiculo2 = Vehiculo("Toyota", "Mustang", 2022)

print(Vehiculo1.obtener_info())
print(Vehiculo2.obtener_info())
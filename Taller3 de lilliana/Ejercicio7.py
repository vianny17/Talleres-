class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def obtener_nombre_completo(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}"

Persona = Persona("Lucia", "Lopez", 18)

print(Persona.obtener_nombre_completo())
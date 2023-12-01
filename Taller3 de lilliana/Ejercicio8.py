class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def obtener_nombre_completo(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}"

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido, edad)
        self.carrera=carrera
    def obtener_nombre_completo(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido} Edad: {self.edad}, Carrera: {self.carrera}")

Estudiante=Estudiante(nombre="Maritza", apellido= "Cortés", edad=23, carrera="Psicologia")

print(Estudiante.obtener_nombre_completo())

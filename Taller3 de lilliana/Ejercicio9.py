class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def obtener_nombre_completo(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}"

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, materia):
        super().__init__(nombre, apellido, edad)
        self.materia=materia
    def obtener_nombre_completo(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, materia: {self.materia}")


Profesor=Profesor(nombre="Carlos", apellido= "Jaramillo", edad="48", materia="Arte")
print(Profesor.obtener_nombre_completo())
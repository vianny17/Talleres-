class Empleado:
    def __init__(self, nombre, apellido, sueldo, beneficios=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.beneficios = beneficios

    def calcular_salario_neto(self):
        impuestos = 0.50
        descuentos = sum(self.beneficios)  

        salario_neto = self.sueldo * (1 - impuestos) - descuentos
        return salario_neto

empleado2 = Empleado(nombre="Rosalba", apellido="Castro", sueldo=70000, beneficios=[4000, 800])

class Programador(Empleado):
    def __init__(self, nombre, apellido, sueldo, beneficios=[], lenguaje=""):
        super().__init__(nombre, apellido, sueldo, beneficios)
        self.lenguaje = lenguaje

    def calcular_salario_neto(self):
        impuestos = 0.20  
        descuentos = sum(self.beneficios)  
        bono_experto = 8000  

        salario_neto_programador = self.sueldo * (1 - impuestos) - descuentos + bono_experto
        return salario_neto_programador

programador1 = Programador(nombre="Mario", apellido="Mosquera", sueldo=90000, beneficios=[6500], lenguaje="Java")

salario_neto_programador1 = programador1.calcular_salario_neto()
print(f"El salario neto del programador {programador1.nombre} {programador1.apellido} es: {salario_neto_programador1}")

class Empleado:
    def __init__(self, nombre, apellido, sueldo, beneficios=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.beneficios = beneficios

    def calcular_salario_neto(self):
        impuestos = 0.48
        descuentos = sum(self.beneficios)  

        salario_neto = self.sueldo * (1 - impuestos) - descuentos
        return salario_neto

empleado2 = Empleado(nombre="Rosalba", apellido="Castro", sueldo=70000, beneficios=[4000, 800])

salario_neto2 = empleado2.calcular_salario_neto()
print(f"El salario neto de {empleado2.nombre} {empleado2.apellido} es: {salario_neto2}")
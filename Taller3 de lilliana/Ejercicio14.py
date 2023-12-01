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

class Gerente(Empleado):
    def __init__(self, nombre, apellido, sueldo, beneficios=[], departamento=""):
        super().__init__(nombre, apellido, sueldo, beneficios)
        self.departamento = departamento

    def calcular_salario_neto(self):
        impuestos = 0.20  
        descuentos = sum(self.beneficios)  
        bono_gerente = 2000  

        salario_neto_gerente = self.sueldo * (1 - impuestos) - descuentos + bono_gerente
        return salario_neto_gerente

gerente1 = Gerente(nombre="Marta", apellido="Gonzales", sueldo=50000, beneficios=[5000], departamento="Ventas")

salario_neto_gerente1 = gerente1.calcular_salario_neto()
print(f"El salario neto del gerente {gerente1.nombre} {gerente1.apellido} es: {salario_neto_gerente1}")
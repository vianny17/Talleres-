def calcular_salario(horas_trabajadas, salario_por_hora):
    if horas_trabajadas > 40:
        horas_normales = 40
        horas_extra = horas_trabajadas - 40
    else:
        horas_normales = horas_trabajadas
        horas_extra = 0

    salario_normal = horas_normales * salario_por_hora

    salario_extra = horas_extra * salario_por_hora * 1.5

    salario_total = salario_normal + salario_extra

    return salario_total

horas_trabajadas = 200
salario_por_hora = 10000

salario = calcular_salario(horas_trabajadas, salario_por_hora)
print(f"El salario total es: ${salario}")

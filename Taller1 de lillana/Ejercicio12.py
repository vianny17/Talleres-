def es_fecha_valida(dia, mes, anio):
    es_bisiesto = (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))

    dias_por_mes = {
        1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if mes < 1 or mes > 12:
        return False

    if mes == 2:
        if es_bisiesto:
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28
    else:
        return 1 <= dia <= dias_por_mes[mes]

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if es_fecha_valida(dia, mes, anio):
    print("La fecha ingresada es válida.")
else:
    print("La fecha ingresada no es válida.")

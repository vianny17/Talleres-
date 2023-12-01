def formato_fecha(dia, mes, anio):
    dia_str = str(dia).rjust(2, '0')  
    mes_str = str(mes).rjust(2, '0') 
    anio_str = str(anio)[-2:] 

    fecha_formateada = f"{dia_str}/{mes_str}/{anio_str}"

    print(fecha_formateada)
dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
anio = int(input("Ingresa el año: "))

formato_fecha(dia, mes, anio)

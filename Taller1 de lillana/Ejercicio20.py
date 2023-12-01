def fusionar_cadenas(mayuscula, minuscula):
    
    mayuscula = mayuscula.upper()
    minuscula = minuscula.lower()
    
    
    cadena_fusionada = mayuscula + minuscula
    
    return cadena_fusionada


cadena_mayuscula = "HOLA\n"
cadena_minuscula = "como estas\n"

resultado = fusionar_cadenas(cadena_mayuscula, cadena_minuscula)
print(resultado)

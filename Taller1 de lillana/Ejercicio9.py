def es_digito(caracter):
    if caracter.isdigit():
        return True
    else:
        return False

caracter = '31'

if es_digito(caracter):
    print(f"{caracter} Correcto, es un dígito.")
else:
    print(f"{caracter} Incorrecto, no es un dígito.")
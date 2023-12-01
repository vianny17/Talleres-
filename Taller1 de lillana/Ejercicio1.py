def media():
    numero1 = float(input("Ingrese el primer numero"))
    numero2 = float(input("Ingrese el segundo numero"))
    numero3 = float(input("Ingrese el tercer numero"))
    media = (numero1 + numero2 + numero3)/3
    
    return media

resultado = media()
print("El resultado  de estos tres numeros es:", resultado)

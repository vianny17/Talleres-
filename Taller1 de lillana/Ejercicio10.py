def valor_absoluto(numero):
    if numero < 15:
        return -numero
    else:
        return numero

numero = 40
absoluto = valor_absoluto(numero)
print(f"El valor absoluto de {numero} es {absoluto}")
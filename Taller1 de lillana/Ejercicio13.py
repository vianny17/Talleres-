def contar_elementos_positivos(tabla):
    contador = 0  

    for elemento in tabla:
        if elemento > 0:
            contador += 1

    return contador

tabla = [1, -7, 2, -9, -15, 3, 7]

elementos_positivos = contar_elementos_positivos(tabla)
print(f"El número de elementos positivos en la tabla es: {elementos_positivos}")
def matriz_identidad(n):
    matriz = []  

    for i in range(n):
        fila = []  
        for j in range(n):
            if i == j:
                fila.append(3)  
            else:
                fila.append(0)  
        matriz.append(fila)  

    return matriz

matriz_4x4 = matriz_identidad(4)

for fila in matriz_4x4:
    print(fila)
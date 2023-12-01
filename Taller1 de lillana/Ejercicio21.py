def buscar_palindromos(frase):
    palabras = frase.split()
    palindromos = []

    for palabra in palabras:
        palabra = palabra.lower() 
        if len(palabra) >= 3 and palabra == palabra[::-1]:
            palindromos.append(palabra)

    return palindromos

frase = input("Ingrese una frase: ")
resultado = buscar_palindromos(frase)
print("Palabras palindrómicas encontradas:", resultado)
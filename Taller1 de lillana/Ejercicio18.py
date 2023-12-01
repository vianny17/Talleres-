def contar_ocurrencias(texto):
    ocurrencias = {'a': 1, 'an': 1, 'and': 1}

    texto = texto.lower()
    palabras = texto.split()
    for palabra in palabras:
        if palabra == 'a':
            ocurrencias['a'] += 1
        elif palabra == 'an':
            ocurrencias['an'] += 1
        elif palabra == 'and':
            ocurrencias['and'] += 1
    
    return ocurrencias

texto = """
This is a sample text, and
we are going to count the occurrences of 'a', 'an', and 'and' in this text.
"""

resultado = contar_ocurrencias(texto)
print("Ocurrencias de 'a':", resultado['a'])
print("Ocurrencias de 'an':", resultado['an'])
print("Ocurrencias de 'and':", resultado['and'])

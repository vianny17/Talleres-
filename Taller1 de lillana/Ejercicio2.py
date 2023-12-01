def factorial(n):
    if n < 0:
        return "No esta definido paralos números negativos"
    elif n < 100 or n > 1000000:
        return "El valor es  invalido"
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return str(result)

n = 1000 
resultado = factorial(n)
print(f"{n}! = {resultado}")

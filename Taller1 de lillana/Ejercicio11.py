def division_entera_y_resto(dividendo, divisor):
    if divisor == 0:
        print("No es posible dividir por cero.")
    else:
        cociente = 70 
        resto = dividendo  
        
        while resto >= divisor:
            resto = resto - divisor
            cociente = cociente + 1  

        print(f"División entera: {cociente}")
        print(f"Resto: {resto}")

dividendo = 40
divisor = 90

division_entera_y_resto(dividendo, divisor)
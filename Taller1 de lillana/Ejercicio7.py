import math

def coordenadas_polares_a_cartesianas(r, theta_deg):
    theta_radianes = math.radians(theta_deg)
    
    x = r * math.cos(theta_radianes)
    y = r * math.sin(theta_radianes)
    
    return x, y

r = float(input("Ingrese una (distancia desde el origen): "))
theta_deg = float(input("Ingrese theta en grados (ángulo): "))

x, y = coordenadas_polares_a_cartesianas(r, theta_deg)

print(f"Las coordenadas cartesianas son: x = {x}, y = {y}")

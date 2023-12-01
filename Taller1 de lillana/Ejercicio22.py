agenda = []
while True:
    nombre = input("Ingrese el nombre y apellido: ")
    ciudad = input("Ingrese la ciudad: ")
    codigo_postal = input("Ingrese el código postal: ")
    telefono = input("Ingrese el teléfono: ")
    edad = input("Ingrese la edad: ")
    
    registro = {
        "nombre": nombre,
        "ciudad": ciudad,
        "codigo_postal": codigo_postal,
        "telefono": telefono,
        "edad": edad
    }
    
    agenda.append(registro)
    
    continuar = input("¿Desea agregar otro registro? (S/N): ")
    if continuar.lower() == "n":
        break
import csv

with open("agenda.csv", "w", newline="") as archivo:
    campos = ["nombre", "ciudad", "codigo_postal", "telefono", "edad"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    escritor.writeheader()
    
    for registro in agenda:
        escritor.writerow(registro)

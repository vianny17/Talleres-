archivo = open('agenda.txt', 'r+')

num_registro = int(input("Ingrese el número de registro a modificar: "))

archivo.seek((num_registro - 1) * 100)
registro_actual = archivo.readline()

print("Registro actual:", registro_actual)

nuevo_nombre = input("Ingrese el nuevo nombre: ")
nuevo_telefono = input("Ingrese el nuevo teléfono: ")
nuevo_email = input("Ingrese el nuevo email: ")

nuevo_registro = f"{nuevo_nombre.ljust(30)}{nuevo_telefono.ljust(30)}{nuevo_email.ljust(40)}\n"

archivo.seek((num_registro - 1) * 100)
archivo.write(nuevo_registro)

archivo.close()

print("Registro modificado con éxito.")
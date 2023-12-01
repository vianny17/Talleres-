archivo_secuencial = open('agenda.txt', 'r')

registros = archivo_secuencial.readlines()

archivo_secuencial.close()

archivo_directo = open('directo_agenda.txt', 'w')

for registro in registros:
    archivo_directo.write(registro)

archivo_directo.close()

print("Archivo copiado con éxito.")


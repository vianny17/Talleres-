archivo = open('agenda.txt', 'r')

registros = archivo.readlines()

for registro in registros:
    print(registro)

archivo.close()




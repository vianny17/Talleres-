estudiantes = {
    'Juan': 4.5,
    'María': 5.0,
    'Pedro': 3.0,
    'Lucía': 2.0,
    'Ana': 3.5
}


media = sum(estudiantes.values()) / len(estudiantes)


print(f'La calificación media es: {media}')

for estudiante, calificacion in estudiantes.items():
    diferencia = calificacion - media
    print(f'{estudiante}: {calificacion}, diferencia con la media: {diferencia}')

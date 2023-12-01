personas={
    "Diego":21,
    "Maria Angel":5,
    "Martha":51,
    "Vianny":18,
    "Sergio":22,
    "Cristian":27
}

mayores= [nombre for nombre, edad in personas.items() if edad > 18 ]

print(mayores)
# Classwork #10 - School Management System
# Solo built-ins: input, print, while, if/elif/else
# Estructuras: listas, diccionarios, tuplas y sets (sin funciones todavia)

# ---------------------------------------------------------
# DATOS
# ---------------------------------------------------------

usuarios = {
    'jperez':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno',      'nombre': 'Ana Martín'},
    'csilva':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Carlos Silva'},
    'lhdez':   {'password': '1234', 'rol': 'alumno',      'nombre': 'Laura Hernández'},
    'dgomez':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Diego Gómez'},
    'fcruz':   {'password': '1234', 'rol': 'alumno',      'nombre': 'Fernanda Cruz'},
    'mlopez':  {'password': '1234', 'rol': 'maestro',     'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'jperez':  {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'csilva':  {'Matemáticas': 6.5, 'Programación': 7.0, 'Inglés': 8.0},
    'lhdez':   {'Matemáticas': 9.5, 'Programación': 9.5, 'Inglés': 9.0},
    'dgomez':  {'Matemáticas': 7.0, 'Programación': 6.5, 'Inglés': 7.0},
    'fcruz':   {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 6.0}
}

# ---------------------------------------------------------
# LOGIN
# ---------------------------------------------------------

acceso = False
while not acceso:
    usuario = input('Usuario: ')
    clave = input('Contraseña: ')

    if usuario in usuarios and usuarios[usuario]['password'] == clave:
        acceso = True
    else:
        print('Usuario o contraseña incorrectos. Intenta de nuevo.\n')

rol = usuarios[usuario]['rol']
nombre = usuarios[usuario]['nombre']
print(f'\nBienvenido, {nombre} ({rol})\n')

# ---------------------------------------------------------
# MENÚ SEGÚN ROL
# ---------------------------------------------------------

if rol == 'alumno':
    print(f'Boleta de {nombre}')

    aprobadas = set()
    for materia in materias:
        calif = calificaciones[usuario][materia]
        print(f'{materia}: {calif}')
        if calif >= 8.0:
            aprobadas.add(materia)

    pendientes = set(materias) - aprobadas

    print('')

    if aprobadas:
        print(f'Materias aprobadas: {aprobadas}')
    else:
        print('Materias aprobadas: Ninguna')

    if pendientes:
        print(f'Materias pendientes: {pendientes}')
    else:
        print('Materias pendientes: Ninguna')

elif rol == 'maestro':
    print('Lista de alumnos:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'alumno':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    continuar = 's'
    while continuar == 's':
        alumno = input('\nAlumno (usuario): ')
        while alumno not in calificaciones:
            print('Ese alumno no existe.')
            alumno = input('Alumno (usuario): ')

        materia = input('Materia: ')
        while materia not in materias:
            print('Esa materia no existe.')
            materia = input('Materia: ')

        nueva_calificacion = float(input('Nueva calificación: '))
        calificaciones[alumno][materia] = nueva_calificacion
        print('Calificación actualizada.')

        continuar = input('\n¿Calificar a otro alumno? (s/n): ')

elif rol == 'coordinador':
    print('Lista de maestros:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'maestro':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    print('\nLista de materias:')
    for materia in materias:
        print(f'- {materia}')

    print('\nLista de alumnos con sus calificaciones:')
    for alumno in calificaciones:
        print(f"\n{usuarios[alumno]['nombre']} ({alumno}):")
        for materia in materias:
            print(f'  {materia}: {calificaciones[alumno][materia]}')
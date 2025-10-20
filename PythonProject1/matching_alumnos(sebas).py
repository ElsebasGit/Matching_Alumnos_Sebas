import csv

datos_alumnos = {}

try:

    with open('Notas_Alumnos_UF1.csv', mode='r', newline='', encoding='latin-1') as archivo_uf1:
        lector_uf1 = csv.DictReader(archivo_uf1, delimiter=';')

        for fila in lector_uf1:
            id_alumno = fila['Id']
            datos_alumnos[id_alumno] = {
                'Id': fila['Id'],
                'Nombre': fila['Nombre'],
                'Apellidos': fila['Apellidos'],
                'UF1': fila['UF1'],
                'UF2': 'No presentada'
            }


    with open('Notas_Alumnos_UF2.csv', mode='r', newline='', encoding='latin-1') as archivo_uf2:
        lector_uf2 = csv.DictReader(archivo_uf2, delimiter=';')

        for fila in lector_uf2:
            id_alumno = fila['Id']
            if id_alumno in datos_alumnos:
                datos_alumnos[id_alumno]['UF2'] = fila['UF2']

    nombres_columnas = ['Id', 'Nombre','Apellidos', 'UF1', 'UF2']

    with open('notas_alumnos.csv', mode='w', newline='', encoding='utf-8') as archivo_salida:
        escritor = csv.DictWriter(archivo_salida, fieldnames=nombres_columnas, delimiter=';')

        escritor.writeheader()
        escritor.writerows(datos_alumnos.values())

    print("El fichero 'notas_alumnos.csv' se ha creado correctamente.")

except FileNotFoundError as e:

    print(
        f"Error: No se pudo encontrar el fichero {e.filename}. Revisa que el nombre coincida exactamente (mayúsculas y minúsculas).")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
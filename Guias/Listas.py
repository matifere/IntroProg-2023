#esto no es para nada necesario, solo queria que me quede bonito el codigo
#todas las listas las hice con ChatGPT, ni en pedo escribo esto yo

listaMedica1 = [
    (5, "Pedro", "Artritis leve"),
    (3, "Carlos", "Hipertensión moderada"),
    (1, "Juan", "Asma grave"),
    (4, "Ana", "Migraña crónica"),
    (7, "Sofía", "Depresión"),
    (2, "Luisa", "Fibromialgia"),
    (6, "María", "Enfermedad de Crohn"),
    (4, "Pablo", "Esclerosis múltiple"),
    (2, "Jorge", "Alergia severa"),
    (6, "Diego", "Esquizofrenia"),
    (5, "Valentina", "Trastorno bipolar"),
    (3, "Gabriela", "Hipotiroidismo"),
    (1, "Andrés", "Obesidad"),
    (7, "Lucía", "Gastritis crónica"),
    (2, "Daniel", "Síndrome de Down")
]
listaMedica2 = [
    (5, "Laura", "Diabetes tipo 2"),
    (7, "Carlos", "Hipertensión arterial"),
    (5, "Ana", "Asma leve"),
    (1, "Pedro", "Migraña crónica"),
    (6, "María", "Artritis reumatoide"),
    (4, "Luis", "Fibromialgia"),
    (2, "Sofía", "Alergia estacional"),
    (4, "Javier", "Esquizofrenia"),
    (1, "Elena", "Depresión mayor"),
    (5, "Diego", "Trastorno de ansiedad"),
    (3, "Lucía", "Hipotiroidismo"),
    (2, "Pablo", "Obesidad"),
    (6, "Valentina", "Síndrome del intestino irritable"),
    (7, "Andrea", "Gastritis crónica"),
    (1, "David", "Enfermedad pulmonar obstructiva crónica")
]
listaMedica3 = [
    (5, "Pedro", "Artritis reumatoide"),
    (3, "María", "Hipertensión arterial"),
    (2, "Juan", "Asma leve"),
    (1, "Sofía", "Migraña crónica"),
    (6, "Carlos", "Fibromialgia"),
    (4, "Ana", "Alergia estacional"),
    (7, "Luisa", "Esquizofrenia"),
    (4, "Elena", "Depresión mayor"),
    (3, "Diego", "Trastorno de ansiedad"),
    (2, "Laura", "Diabetes tipo 2"),
    (6, "Gabriel", "Hipotiroidismo"),
    (5, "Valentina", "Obesidad"),
    (1, "Andrés", "Síndrome del intestino irritable"),
    (7, "Lucía", "Gastritis crónica"),
    (1, "Javier", "Enfermedad pulmonar obstructiva crónica"),
    (5, "Camila", "Epilepsia"),
    (3, "Marcelo", "Hemofilia"),
    (2, "Florencia", "Fibrosis quística"),
    (6, "Miguel", "Psoriasis"),
    (4, "Isabella", "Esclerosis múltiple")
]

#lo siguiente es para generar un csv

import csv
import random

materias_exactas = [
    "Álgebra",
    "Cálculo",
    "Geometría",
    "Estadística",
    "Física",
    "Química",
    "Biología",
    "Programación",
    "Matemáticas aplicadas",
    "Investigación operativa",
    "Probabilidad",
    "Álgebra lineal",
    "Topología",
    "Optimización",
    "Mecánica cuántica"
]

alumnos = []
num_materias = len(materias_exactas)

for i in range(1, 101):
    lu = f"LU{i:03}"
    materias = random.sample(materias_exactas, random.randint(3, num_materias))
    fecha = "2023-01-01"  # Fecha de ejemplo

    for materia in materias:
        nota = round(random.uniform(4.0, 10.0), 1)  # Generar nota aleatoria entre 4.0 y 10.0
        alumnos.append((lu, materia, fecha, nota))

with open("alumnos.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["nro de LU", "materia", "fecha", "nota"])
    writer.writerows(alumnos)

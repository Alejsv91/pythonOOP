import pandas as pd
import csv
from estudiantes import Estudiantes
from estudiante import Estudiante
from materia import Materia

archivo_nombre = 'estudiantes.csv'

def exportar_datos_csv(estudiantes: Estudiantes):
    with open(archivo_nombre, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        titles = ["Nombre", "Seccion", "Promedio"] 
        materias = estudiantes.lista[0].obtener_nombre_materias()
        titles.extend(materias)
        writer.writerow(titles)
        
        for estudiante in estudiantes.lista:
            fila = [
                estudiante.nombre,
                estudiante.seccion,
                estudiante.promedio
            ]
            notas = estudiante.obtener_notas_materias()
            fila.extend(notas)
            writer.writerow(fila)
    print("csv de estudiantes creado")
    
def importar_datos_csv():
    lista = []
    df = pd.read_csv(archivo_nombre)
    for _, row in df.iterrows():
        nombre = row['Nombre']
        seccion = row['Seccion']
        promedio = row['Promedio']
        
        materias = [
            Materia("Español", row["Español"]),
            Materia("Ingles", row["Ingles"]),
            Materia("Sociales", row["Sociales"]),
            Materia("Ciencias", row["Ciencias"]),
        ]
        
        estudiante = Estudiante(nombre=nombre, 
                                seccion=seccion, 
                                promedio=promedio,
                                materias=materias)
        
        lista.append(estudiante)
        print('Datos importados')
        
    return Estudiantes(lista)
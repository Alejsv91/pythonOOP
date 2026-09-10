import pandas as pd
import csv
from estudiantes import Estudiantes

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
    df = pd.read_csv(archivo_nombre)
    print(df)
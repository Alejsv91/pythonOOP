from estudiantes import Estudiantes
from estudiante import Estudiante


def agregar_estudiantes(estudiantes: Estudiante):
    estudiantes.agregar_estudiante()
    return estudiantes
            
def mostrar_estudiantes(estudiantes: Estudiantes):
    estudiantes.mostrar_estudiantes()

def mostrar_top_3_promedios(estudiantes: Estudiantes):    
    estudiantes.mostrar_top_tres_por_promedio()
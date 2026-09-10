from materia import Materia
from functools import reduce

class Estudiante:
    nombre: str
    seccion: str
    materias = [Materia]
    promedio: int
    
    def __init__(self):
        self.nombre = input("Nombre completo del estudiante:")
        self.seccion = input("Seccíon:")
        self.materias = [Materia('Español'), Materia('Ingles'), Materia('Sociales'), Materia('Ciencias')]
        self.sacar_promedio()
    
    def mostrar_info_estudiante(self):
        print('-------------------------------------------------')
        print(f'Nombre del Estudiante: {self.nombre}')
        print(f'Sección: {self.seccion}')
        for materia in self.materias:
            print(f"Nota de {materia.nombre}: {materia.nota}")
        print(f'El promedio del estudiante es: {self.promedio}')
        print('-------------------------------------------------')
    
    def sacar_promedio(self):
        self.promedio = reduce(lambda acc, materia: acc + materia.nota, self.materias, 0) / len(self.materias)
        
        
        
class Estudiantes:
    lista: list[Estudiante]
    
    def __init__(self):
        self.lista = []
        
    def mostrar_estudiantes(self):
        for estudiante in self.lista:
            estudiante.mostrar_info_estudiante()
            
    def mostrar_top_tres_por_promedio(self):
        self.lista_ordenada =sorted(self.lista, key=lambda estudiante: estudiante.promedio, reverse=True)
        for i, estudiante in enumerate(self.lista_ordenada):
            print(f"""Posición {i + 1} es para el estudiante {estudiante.nombre} con el promedio de { estudiante.promedio}""")
            if not(i < 2):
                break
        
agregar_estudiantes = True
estudiantes = Estudiantes()
         
while agregar_estudiantes == True:
    estudiantes.lista.append(Estudiante())
    
    if(input("Desea agregar otro estudiante? (si/no):").lower()  == 'si'):
        agregar_estudiantes = True
    else:
        agregar_estudiantes = False       
        
if(input('Desea ver la lista de estudiantes? (si/no): ' ).lower() == 'si'):
    estudiantes.mostrar_estudiantes()

if(input('Desea ver el top 3 de promedios? (si/no): ' ).lower() == 'si'):
    estudiantes.mostrar_top_tres_por_promedio()
    
    
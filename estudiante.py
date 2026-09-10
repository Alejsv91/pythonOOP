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
        
    def obtener_nombre_materias(self):
        return list(map(lambda m: m.nombre, self.materias))
    
    def obtener_notas_materias(self):
        return list(map(lambda m: m.nota, self.materias))
        
        

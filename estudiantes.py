class Estudiante:
    nombre: str
    seccion: str
    nota_espanol: int
    nota_ingles: int
    nota_sociales: int
    nota_ciencias: int
    promedio: int
    
    def __init__(self, nombre: str, seccion: str, nota_espanol: int, nota_ingles: int, nota_sociales: int,  nota_ciencias: int):
        self.nombre = nombre
        self.seccion = seccion
        
        self.notas = [int(nota_ciencias), int(nota_espanol), int(nota_ingles), int(nota_sociales)]
        
        if not all(isinstance(x, int) for x in self.notas):
            raise ValueError('Todas las notas deben de ser valores numericos y tener un valor mayor a cero y menor o igual a 100')
        
        if not all(x >= 0 and x <=100 for x in self.notas):
            raise ValueError('Las notas deben de tener un valor mayor o igual a cero y menor o igual a 100')
        
        self.nota_espanol = self.notas[1]
        self.nota_ingles = self.notas[2]
        self.nota_sociales = self.notas[3]
        self.nota_ciencias = self.notas[0]
        self.promedio = sum(self.notas) / len(self.notas)
        
class Estudiantes:
    lista: list[Estudiante]
    
    def __init__(self):
        self.lista = []
        
    def mostrar_estudiantes(self):
        for estudiante in self.lista:
            print(f"""
- Nombre: {estudiante.nombre}
-- Notas:
--- Español: {estudiante.nota_espanol}
--- Ingles: {estudiante.nota_ingles}
--- Sociales: {estudiante.nota_sociales}
--- Ciencias: {estudiante.nota_ciencias}""")
            
    def mostrar_top_tres_por_promedio(self):
        self.lista_ordenada =sorted(self.lista, key=lambda estudiante: estudiante.promedio, reverse=True)
        for i, estudiante in enumerate(self.lista_ordenada):
            print(f"""Posición {i + 1} es para el estudiante {estudiante.nombre} con el promedio de { estudiante.promedio}""")
            if not(i < 2):
                break
        
agregar_estudiantes = True
estudiantes = Estudiantes()
         
while agregar_estudiantes == True:
    nombre = input("Nombre completo del estudiante:")
    seccion = input("Seccíon:")
    nota_espanol = input("Nota de español:")
    nota_ingles = input("Nota de ingles:")
    nota_sociales = input("Nota de sociales:")
    nota_ciencias = input("Nota de ciencias:")
    estudiantes.lista.append(Estudiante(nombre, seccion, nota_espanol, nota_ingles, nota_sociales, nota_ciencias))
    
    if(input("Desea agregar otro estudiante? (si/no):").lower()  == 'si'):
        agregar_estudiantes = True
    else:
        agregar_estudiantes = False       
        
if(input('Desea ver la lista de estudiantes? (si/no): ' ).lower() == 'si'):
    estudiantes.mostrar_estudiantes()

if(input('Desea ver el top 3 de promedios? (si/no): ' ).lower() == 'si'):
    estudiantes.mostrar_top_tres_por_promedio()
    
    
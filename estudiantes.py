from estudiante import Estudiante

class Estudiantes:
    lista: list[Estudiante]
    
    def __init__(self, lista = list[Estudiante] | None):
        self.lista = [] if list is None else lista
    
    def agregar_estudiante(self):
        agregar_estudiantes = True
        
        while agregar_estudiantes == True:
            self.lista.append(Estudiante())
            print("Estudiante agreado")
        
            if(input("Desea agregar otro estudiante? (si/no):").lower()  == 'si'):
                agregar_estudiantes = True
            else:
                agregar_estudiantes = False
        
        
    def mostrar_estudiantes(self):
        for estudiante in self.lista:
            estudiante.mostrar_info_estudiante()
            
    def mostrar_top_tres_por_promedio(self):
        self.lista_ordenada =sorted(self.lista, key=lambda estudiante: estudiante.promedio, reverse=True)
        for i, estudiante in enumerate(self.lista_ordenada):
            print(f"""Posición {i + 1} es para el estudiante {estudiante.nombre} con el promedio de { estudiante.promedio}""")
            if not(i < 2):
                break
        

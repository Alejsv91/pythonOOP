from estudiantes import Estudiantes
from data import exportar_datos_csv

estudiantes = Estudiantes()
error_opcion_invalida = """\033[91m
--------ERROR--------
Debe de seleccionar una opción del 1 al 5
---------------------\033[0m"""

error_sistema = """\033[91m
--------ERROR--------
Solo puede agregar valores númericos
---------------------\033[0m"""

menu="""
Opciones:
    1. Agregar estudiante.
    2. Mostrar lista de estudiantes
    3. Mostrar top 3 de mejores promedios
    4. Crear csv
    5. Salir
Seleccione una opción: """
            
def iniciar_menu():
    agregar_estudiantes = True
    opcion = 0
    
    while not opcion == 5:
        print('---------- Menú principal ----------')
        try: 
            opcion = int(input(menu))
            
            if opcion not in range(1, 6):
                print(error_opcion_invalida)
                
            else:
                print(f'Ejecutando opcion {opcion}')
                ejecutar_accion(opcion)
                
        except Exception as e: 
            print(error_sistema)
            print(f"Error: {type(e).__name__}")
            print(e)

def ejecutar_accion(opcion: int):
    match opcion:
        case 1:
            estudiantes.agregar_estudiante()
        case 2:
            estudiantes.mostrar_estudiantes()
        case 3: 
            estudiantes.mostrar_top_tres_por_promedio()
        case 4: 
            exportar_datos_csv(estudiantes)
        case 5:
            print("Finalizando...")
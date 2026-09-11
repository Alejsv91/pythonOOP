from estudiantes import Estudiantes
from data import exportar_datos_csv, importar_datos_csv

error_opcion_invalida = """\033[91m
--------ERROR--------
Debe de seleccionar una opción del 1 al 5
---------------------\033[0m"""

error_sistema = """\033[91m
--------ERROR--------
Error interno del sistema
---------------------\033[0m"""

menu="""
Opciones:
    1. Agregar estudiante.
    2. Mostrar lista de estudiantes
    3. Mostrar top 3 de mejores promedios
    4. Crear csv
    5. Importar estudiantes de csv
    6. Salir
Seleccione una opción: """
            
def iniciar_menu():
    opcion = 0
    estudiantes = Estudiantes()
    
    while not opcion == 6:
        print('---------- Menú principal ----------')
        try: 
            opcion = int(input(menu))
            
            if opcion not in range(1, 7):
                print(error_opcion_invalida)
                
            else:
                print(f'Ejecutando opcion {opcion}')
                estudiantes = ejecutar_accion(opcion, estudiantes)
                
        except Exception as e: 
            print(error_sistema)
            print(f"Error: {type(e).__name__}")
            print(e)

def ejecutar_accion(opcion: int, estudiantes: Estudiantes):
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
            estudiantes = importar_datos_csv()
        case 6:
            print("Finalizando...")
    
    return estudiantes
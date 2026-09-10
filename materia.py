class Materia:
    nombre: str
    nota: int
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.nota = self.validar_nota(nombre)
    
    def validar_nota(self, nombre: str):
        nota_valida = False
        while not nota_valida:
            try:
                nota = int(input(f"Ingrese la nota de {nombre}: "))
                if 0 <= nota <= 100:
                    nota_valida = True
                    return nota
                else:
                    print("La nota ingresada no es valida, tiene que ser un número mayor igual a 0 y menor igual a 100")
            except:
                print("Valor en la nota no es valido, ingrese un valor númerico")
                
            
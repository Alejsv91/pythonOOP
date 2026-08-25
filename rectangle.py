class Rectangle:
    width: float
    height: float
    
    def __init__(self, width: float, height: float):
        
        self.width = float(width)
        self.height = float(height)
        
        if(self.width < 0 or self.height < 0):
            raise TypeError("Existe un valor negativo, los valores deben ser positivos")
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
width = input("Ingrese la base del rectangulo: ")
height = input("Ingrese la altura del rectangulo:")
    
rec1 = Rectangle(width, height)

print(f"El area del rectangulo es: {rec1.get_area()}")
print(f"El perimetro es: {rec1.get_perimeter()}")

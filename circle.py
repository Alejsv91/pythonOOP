import math

class Circle:
    radius = 10

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        print(f"El area del circulo es de: {area}")
        return area


circle = Circle()
circle.get_area()
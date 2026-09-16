from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    radius: float
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return (2 * pi) * self.radius
    
    def calculate_area(self):
        return pi * (self.radius ** 2)

class Square(Shape):
    side: float
    
    def __init__(self, side: float):
        self.side = side
        
    def calculate_perimeter(self):
        return self.side * 4
    
    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape):
    width: float
    height: float
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    
    
    
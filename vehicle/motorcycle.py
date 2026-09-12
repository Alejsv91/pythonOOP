from .vehicle import Vehicle

class Motorcycle(Vehicle):
    _type: str
    _color: str
    
    def __init__(self, type: str, color: str, brand: str, year: int):
        super().__init__(brand, year)
        self.type = type
        self.color = color
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
        
    
    def get_info(self):
        print(f"{self.brand} ({self.year}) - type: {self.type} - color: {self.color}")
        
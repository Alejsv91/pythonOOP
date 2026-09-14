from .vehicle import Vehicle

class Car(Vehicle):
    _doors: int
    _type: str
    
    def __init__(self, doors: int, type: str, brand: str, year: str | int):
        self.doors = doors
        self.type = type
        super().__init__(brand, year)
    
    @property
    def doors(self):
        return self._doors
    
    @doors.setter
    def doors(self, value):
        self._doors = value
    
    @property
    def type(self):
        return self._type 
    
    @type.setter
    def type(self, value):
        self._type = value
    
    def get_info(self):
        print(f"{self.brand} ({self.year}) - doors:{self.doors} - type: {self.type}")
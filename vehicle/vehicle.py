from abc import ABC, abstractmethod

class Vehicle(ABC):
    _brand: str
    _year: int
    
    def __init__(self, brand: str, year: str | int):
        self.brand = brand
        self.year = year
        print("Vehicle created")
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def year(self):
        return self._year
    
    @brand.setter
    def brand(self, value):
        self._brand = value
        
    @year.setter
    def year(self, value: str | int):
        self._year = int(value)
    
    @abstractmethod
    def get_info(self):
        print(f"{self.brand} ({self.year})")
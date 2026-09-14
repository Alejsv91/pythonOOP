from .car import Car
from .motorcycle import Motorcycle

car = Car(4, 'Sedan', "Toyota", 2024)
motorcycle = Motorcycle("Sport", "Blue", "Yamaha", 2010)

car.get_info()
motorcycle.get_info()
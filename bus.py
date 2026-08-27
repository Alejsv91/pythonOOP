
class Person():
    
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0
    
class Bus:
    
    max_passengers: int
    passenger_list: list
    
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passenger_list = []
        print(f'Bus creado con capacidad de: {self.max_passengers} pasajeros')
    
    def add_passenger(self, person: Person):
        if(self.max_passengers > len(self.passenger_list)):
            self.passenger_list.append(person)
            print(f"Pasajero {person.name} se subío al bus")
        else:
            print(f"Pasajero {person.name} no se pudo subir al bus. El bus está en su capacidad maxima")
    
    def remove_passenger(self, person: Person):
        self.passenger_list.remove(person)
        print(f"Pasajero {person.name} se bajo del bus, espacios disponibles: {self.max_passengers - len(self.passenger_list)}")
        
        print('Pasajeros montados en el bus:')
        for p in self.passenger_list:
            print(f"--Nombre pasajero: {p.name}")
        
            
passenger1 = Person('Luis')
passenger2 = Person('Ana')
passenger3 = Person('Rodrigo')
passenger4 = Person('Josue')
bus1 = Bus(3)

bus1.add_passenger(passenger1)
bus1.add_passenger(passenger2)
bus1.add_passenger(passenger3)
bus1.add_passenger(passenger4)

bus1.remove_passenger(passenger1)

            
            
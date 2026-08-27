class Animal:
    name: str
    
    def __init__(self, name: str):
        self.name = name
    
    def speak(self):
        return "Hace un sonido"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"
    
dog_name = input("Introduzca un nombre para perro: ")
cat_name = input("Introduzca un nombre para un gato: ")

dog = Dog(dog_name)
cat = Cat(cat_name)

print(dog.speak())
print(cat.speak())
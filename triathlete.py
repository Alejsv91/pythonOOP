class Person:
    pass

class Swimmer:
    def swim(self):
        return "Swimming..."

class Cyclist:
    def cycle(self):
        return "Cycling..."
    
class Runner:
    def run(self):
        return "Running"

class Triathlete(Person, Swimmer, Cyclist, Runner):
    pass


# Este sería el ejemplo de herencia multiple, en este tipo de eventos se necesitan 3 tipos de deportes. Cada deporte representa una clase la cual tiene sus atributos y metodos específicos
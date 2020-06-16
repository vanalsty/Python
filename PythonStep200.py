
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
        
class Llama(Animal):
    def eat(self):
        print("Llama eats hay.")

class Dog(Animal):
    def eat(self):
        print("Dog eats kibble.")



l=Llama()
l.eat()

d=Dog()
d.eat()


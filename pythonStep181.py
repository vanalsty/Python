class Animal:
    def __init__(self, name=''):
        self.name = name
    def talk(self):
        pass
    
class Llama(Animal):
    def __init__(self, name=""):
        super().__init__(name)
    def talk(self):
        print(self.name, "hums!")
    def looks(self):
        print(self.name, "has soft, fluffy fiber!")
    def action(self):
        print(self.name, "spits when mad.")

class Pig(Animal):
    def __init__(self, name=""):
        super().__init__(name)
    def talk(self):
        print(self.name, "says Oink!")
    def play(self):
        print(self.name, "rolls in mud!")
    def eats(self):
        print(self.name, "eats slop.")

a = Animal()
a.talk()

l = Llama("Rojo")
l.talk()
l.looks()
l.action()

p = Pig("Babe")
p.talk()
p.play()
p.eats()

input()
    





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
        furColor = "brown"
        height = "6 feet"
        print(self.name, "has soft,", furColor, ",fluffy fiber!")

class Pig(Animal):
    def __init__(self, name=""):
        super().__init__(name)
    def talk(self):
        print(self.name, "says Oink!")
    def play(self):
        skinColor = "pink"
        weight = "500 lbs"
        print(self.name, "is", skinColor, "weighs", weight, "and rolls in mud!")



a = Animal()
a.talk()

l = Llama("Rojo")
l.talk()
l.looks()


p = Pig("Babe")
p.talk()
p.play()


input()
    





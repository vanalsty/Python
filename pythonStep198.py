class employee:
    def __init__(self, name, sal):
        self._name=name 
        self.__salary=sal

    def myfunc(self):
        print("Hello, my name is " + e1._name + " and I make ",e1.__salary, "dollars a year.")
        
e1=employee("Laurie", 100000)
e1.myfunc()




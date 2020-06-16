class employee:
    def __init__(self, name, sal):
        self._name=name 
        self.__salary=sal 
        
e1=employee("Laurie", 100000)
print(e1._name)
print(e1.__salary)


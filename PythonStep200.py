from abc import ABC, abstractmethod

class Basic_info(ABC):
    def __init__(self):
        self.name=""
        self.age =0
        self.u_id=0
    def accept(self):
        self.name = input("Enter Name:  ")
        self.age = int(input("Enter Age:  "))
        self.user_id = input("Enter UserID:  ")
    def display(self):
        print(self.name)
        print(self.age)
        print(self.user_id)
        
    @abstractmethod
    def Accept_Basic_info(self):
        pass

    @abstractmethod
    def Display_basic_info(self):
        pass

class student(Basic_info):
    def __init__(self):
        self.roll_no = 0
        self.Class = 0
        self.section = 0


    def Accept_Basic_info(self):
        self.accept()
        self.roll_no = input("Enter roll No:  ")
        self.Class = input("Enter class:  ")
        self.section = input("Enter section:  ")

    def Display_basic_info(self):
        self.display()
        print(self.roll_no)
        print(self.Class)
        print(self.section)

class teacher(Basic_info):
    def __init__(self):
        self.subject = 0
        self.shift = 0

    def Accept_Basic_info(self):
        self.accept()
        self.subject = input("Enter Subject: ")
        self.shift = input("Enter Shift: ")

    def Display_basic_info(self):
        self.display()
        print(self.subject)
        print(self.shift)

a=student()
print("Student")
a.Accept_Basic_info()
a.Display_basic_info()

b=teacher()
print("Teacher")
b.Accept_Basic_info()
b.Display_basic_info()

# Example of Inheritance in python

class Person:

    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print('My name is {}'.format(self.name))
        print('IdNumber: {}'.format(self.idnumber))


class Child(Person):
    
    def __init__(self, name, idnumber, salary):
        super().__init__(name, idnumber)
        self.salary=salary

    def display(self):
        super().display()
        print('Salary:{}'.format(self.salary))



a= Child('Prijal', 210, 3244)
a.display()
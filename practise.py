class Person:

    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber



    def display(self):
        print("My name is {}".format(self.name))
        print("IdNumber:{}".format(self.idnumber))


a= Person('Prijal', 210)

a.display()

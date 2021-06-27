class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)


personObject = Person("Tommy", 23)

del personObject
personObject.print_age()
personObject.print_name()

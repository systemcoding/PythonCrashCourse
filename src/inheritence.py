class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 1
        self.y += 1
        print(self.x, self.y)


class Student(Person):
    def __init__(self, x, y):
        super().__init__(x, y)


studentObj = Student(2, 3)
studentObj.move()

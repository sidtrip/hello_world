class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.marks)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name, self.age, self.salary)


s = Student('Rida', 20, 250)

s.display()

e = Employee('Harsh', 30, 50000)
e.display()




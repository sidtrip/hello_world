class Student:
    count = 0    
    def __init__(self, roll_no, name, total):
        self.roll_no = roll_no
        self.name = name
        self.total = total

    def display(self):
        print(self.roll_no, self.name, self.total)

    def result(self):
        if self.total > 120:
            print('Pass')
        else:
            print('Fail') 


s0 = Student(0, 'Bhuvanesh', 100)
s0.display()
Student.count += 1
s0.result()

s1 = Student(1, 'Harish', 150)
Student.count += 1
s1.display()
s1.result()

print(Student.count)





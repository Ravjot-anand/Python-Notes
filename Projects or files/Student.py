class Student :
    def __init__(self, name, age, grade , is_on_probation):
        self.name = name
        self.age = age
        self.grade = grade #grade is 0-100
        self.is_on_probation = is_on_probation
        
    def is_on_honor_roll(self):
        if self.grade >= 75:
            return True
        else:
            return False

'''
Example of creating an object of Student class
in student.py file and accessing its attributes
from Student import Student
'''
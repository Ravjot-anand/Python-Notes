from Student import Student

student1 = Student("Jim", 15, 95, False)    
student2 = Student("Pam", 14, 65, True)

print(student1.name)
print(student1.age)     
print(student1.grade)
print(student1.is_on_probation) 

print("\n")

print(student1.is_on_honor_roll())
print(student2.is_on_honor_roll())

'''
Example of creating an object of Student class
in app.py file and accessing its attributes
'''
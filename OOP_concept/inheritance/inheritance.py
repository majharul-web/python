class Person :
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    def __repr__(self):
        return(f'This person name is {self.name} and he is a {self.gender}')

person_1=Person('Jahir','Male')
print(person_1)

class Student(Person):
    def __init__(self,name,gender):
        super().__init__(name,gender)
        self.type="Student"
    
    def __repr__(self):
        return f'This person name is {self.name} and he is a {self.gender} also a {self.type}'
    
student_1=Student('Karim','Male')
print(student_1)



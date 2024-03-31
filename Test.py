class Student:
    
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    def get_Info(self):
        print("Name: ", self._name)
        print("Age: ", self._age)
        print("Grade: ", self._grade)

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self._grade = grade
            
    def setinfo(self, name, age):
        self._name = name
        self._age = age

student1 = Student("Clark", 18, 90)
    
student1.get_Info()

print("\nGrade updated to 80")
student1.set_grade(80)
student1.get_Info()

print("\n")
student1.__init__("Loli",50,99)
student1.get_Info()

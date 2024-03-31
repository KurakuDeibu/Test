class Student:


    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    def get_Info(self):
        print("Name: ", _name)
        print("Age: ", _age)
        print("Grade: ", _grade)

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self._grade = grade

    student1 = Student("Clark", 18, 90)

    
    student1.get_Info()

    student1.set_grade(80)

    student1.get_Info()


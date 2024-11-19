class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def set_details(self, new_name, new_age, new_gender):
        self.name = new_name
        self.age = new_age
        self.gender = new_gender

    def get_details(self, new_name, new_age, new_gender):
        print("Name: " + new_name + ", Age: " + new_age + ", Gender: " + new_gender)


class Student(Person):
    def __init__(self, name, age, gender, student_id, course, grades):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.grades = grades

    def set_student_details(self, new_student_id, new_course):
        self.student_id = new_student_id
        self.course = new_course

    def add_grade(self, new_grade):
        self.grades = new_grade

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0 
        total = sum(self.grades)
        total = total / len(self.grades)
        print("Average grade is " + total)

    def get_student_summary(self):
        




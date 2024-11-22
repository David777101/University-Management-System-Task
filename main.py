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
        return total

    def get_student_summary(self, new_course, new_grade, total, new_student_id):
        return new_course, new_grade, total, new_student_id
    

class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def set_professor_details(self, new_staff_id, new_department, new_salary):
        self.staff_id = new_staff_id
        self.new_department = new_department
        self.new_salary = new_salary

    def give_feedback(self, student, feedback):
        print("Feedback for " + student + " : " + feedback)

    def increase_salary(self, percentage, salary):
        salary = salary * (1 + (percentage/100))

    def get_professor_summary(self, new_staff_id, new_department, new_salary):
        return new_staff_id, new_department, new_salary

class Administrator(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(self, name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def set_admin_details(self, new_admin_id, new_office, new_years_of_service):
        self.admin_id = new_admin_id
        self.office = new_office
        self.years_of_service = new_years_of_service

    def increment_service_years(self, new_years_of_service):
        new_years_of_service = new_years_of_service + 1

    def get_admin_summary(self, new_admin_id, new_office, new_years_of_service):
        return new_admin_id, new_office, new_years_of_service


object1 = Student("Fred" , 18 , "Male", 1234, "Biology", "876598", )
object2 = Student("Georgia" , 19 , "Female", 5678, "Physics", "8761234", )

object3 = Administrator("George", )
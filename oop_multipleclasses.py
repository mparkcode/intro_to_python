class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def student_info(self):
        return f"Student: {self.name}, Age: {self.age}, grade: {self.grade}"
    
    def get_grade(self):
        return self.grade
    

class Course:
    # have a name
    # have a maximum number of students
    # to be able to add a student to a course
    # return the average grade
    
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

    
    
s1 = Student('Adam', 20, 95)
s2 = Student('Barbara', 19, 80)
s3 = Student ('David', 21, 74)

my_course = Course('Science', 2)
my_course.add_student(s1)
my_course.add_student(s2)
my_course.add_student(s3)
print(my_course.get_average_grade())
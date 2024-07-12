list_curse_grades_student = {}
list_curse_grades_lecturer = {}

class Student:
    def __init__(self, name, surname, gender, grade_courses):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progres = []
        self.grades = {}
        self.grade_courses = grade_courses
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 
        
    def rate_Lecturer(self, lecturer, course, grade):
        global list_curse_grades_lecturer 
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progres and course in lecturer.grade_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                if course in list_curse_grades_lecturer:
                    list_curse_grades_lecturer[course] += [grade]
                else:
                    list_curse_grades_lecturer[course] = [grade]
            else:
                lecturer.grades[course] = [grade]
                if course in list_curse_grades_lecturer:
                    list_curse_grades_lecturer[course] += [grade]
                else:
                    list_curse_grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):            
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {round(sum(self.grades[self.grade_courses]) / len(self.grades[self.grade_courses]), 1)} \n" \
               f"Курсы в процессе изучения: {self.courses_in_progres} \n" \
               f"Завершенные курсы: {self.finished_courses}" 
    def __eq__(self, other: "Student"):
        object1 = sum(self.grades[self.grade_courses]) / len(self.grades[self.grade_courses])
        object2 = sum(other.grades[other.grade_courses]) / len(other.grades[other.grade_courses])
        result = object1 - object2
        if result > 0:
            return(f'Средняя оценка выше у {self.name}')
        elif result < 0:
            return(f'Средняя оценка выше у {other.name}')
        else:
            return("Одинаково")
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
class Lecturer(Mentor):
    def __init__(self, name, surname, grade_courses):
        super().__init__(name, surname)
        self.grade_courses = grade_courses
        self.grades = {}
    
    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {round(sum(self.grades[self.grade_courses]) / len(self.grades[self.grade_courses]), 1)}"
    
    def __eq__(self, other: "Lecturer"):
        object1 = sum(self.grades[self.grade_courses]) / len(self.grades[self.grade_courses])
        object2 = sum(other.grades[other.grade_courses]) / len(other.grades[other.grade_courses])
        result = object1 - object2
        if result > 0:
            return(f'Средняя оценка выше у {self.name}')
        elif result < 0:
            return(f'Средняя оценка выше у {other.name}')
        else:
            return("Одинаково")
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        global list_curse_grades_student 
        if isinstance(student, Student) and course in student.courses_in_progres:
            if course in student.grades:
                student.grades[course] += [grade]
                if course in list_curse_grades_student:
                    list_curse_grades_student[course] += [grade]
                else:
                    list_curse_grades_student[course] = [grade]
            else:
                student.grades[course] = [grade]
                if course in list_curse_grades_student:
                    list_curse_grades_student[course] += [grade]
                else:
                    list_curse_grades_student[course] = [grade]
        else:
             return 'Ошибка'
    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname}"

def average_grades(_class, course):
    global list_curse_grades_lecturer
    global list_curse_grades_student
    if _class ==  Student:
        print(f'Средняя оценка за курс {round(sum(list_curse_grades_student[course]) / len(list_curse_grades_student[course]))}')
    elif _class == Lecturer:
        print(f'Средняя оценка за курс {round(sum(list_curse_grades_lecturer[course]) / len(list_curse_grades_lecturer[course]))}')    
 
 
student1 = Student('Ruoy', 'Eman', 'your_gender', 'Python')
student2 = Student('Steve', 'Rogers', 'your_gender', 'Python')

student1.courses_in_progres += ['Python']
student2.courses_in_progres += ['Python']


cool_Reviewer = Reviewer('Tom', 'Riddle')
Lecturer1 = Lecturer('Buddy', 'Some', 'Python')
Lecturer2 = Lecturer('Some', 'Buddy', 'Python')
 
student1.rate_Lecturer(Lecturer1, 'Python', 10)
student1.rate_Lecturer(Lecturer2, 'Python', 9)
student2.rate_Lecturer(Lecturer1, 'Python', 9)
student2.rate_Lecturer(Lecturer2, 'Python', 10)
 
cool_Reviewer.rate_hw(student1, 'Python', 10)
cool_Reviewer.rate_hw(student1, 'Python', 8)
cool_Reviewer.rate_hw(student1, 'Python', 10)
cool_Reviewer.rate_hw(student2, 'Python', 8)
cool_Reviewer.rate_hw(student2, 'Python', 10)
cool_Reviewer.rate_hw(student2, 'Python', 9)

print(student1)
print(student2)
print(Lecturer1)
print(Lecturer2)
print(cool_Reviewer)
print(student1 == student2)
print(Lecturer1 == Lecturer2)
average_grades(Student, 'Python')
average_grades(Lecturer, 'Python')

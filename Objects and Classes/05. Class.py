class Class:
    __students_count = 22
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if self.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(float(grade))
            return self.students and self.grades and Class.__students_count

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return round(average_grade, 2)

    def __repr__(self):
        students_list = ', '.join(self.students)
        result = f"The students in {self.name}: {students_list}. Average grade: {self.get_average_grade()}"
        return result

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
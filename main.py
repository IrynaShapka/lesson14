# Визначення класу Human
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

# Визначення класу Student, що наслідує Human
class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record Book: {self.record_book}"

# Визначення винятку користувача GroupFullError
class GroupFullError(Exception):
    def __init__(self, message="Group is full. Cannot add more students."):
        self.message = message
        super().__init__(self.message)

# Визначення класу Group
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullError
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Group Number: {self.number}\n{all_students}'

# Тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN143')
st4 = Student('Female', 23, 'Jane', 'Doe', 'AN144')
st5 = Student('Male', 21, 'Mike', 'Johnson', 'AN146')
st6 = Student('Female', 24, 'Emily', 'Davis', 'AN147')
st7 = Student('Male', 20, 'Chris', 'Brown', 'AN148')
st8 = Student('Female', 26, 'Anna', 'Smith', 'AN149')
st9 = Student('Male', 28, 'James', 'Wilson', 'AN150')
st10 = Student('Female', 27, 'Mary', 'Lee', 'AN151')
st11 = Student('Male', 29, 'David', 'Clark', 'AN152')

gr = Group('PD1')
students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

for student in students:
    try:
        gr.add_student(student)
    except GroupFullError as e:
        print(e)

print(gr)

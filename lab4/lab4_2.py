class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section 
        self.credit = credit
        self.student_list = []
        self.teacher = None ##single teacher

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

stu1 = Student("66010001", "Ja")
stu2 = Student("66010002", "Cat")
stu3 = Student("66010003", "Apple")
stu4 = Student("66010004", "Fah")
stu5 = Student("66010005", "Win")

tea1 = Teacher("10", "Henry")
tea2 = Teacher("20", "Devid")

oop16 = Subject("010760105", "oop sec16", "16", "3")
oop17 = Subject("010760106", "oop sec17", "17", "3")

subjects = [oop16, oop17]

oop16.student_list.append(stu1)
oop16.student_list.append(stu2)
oop17.student_list.append(stu3)
oop17.student_list.append(stu4)
oop17.student_list.append(stu5)
oop16.teacher = tea1
oop17.teacher = tea2

def search_students_by_teacher_id(teacher_id):
    student_list_learn = []
    for subject in subjects:
        if subject.teacher.teacher_id == teacher_id:
            for stu in subject.student_list:
                student_list_learn.append(stu.student_name)
    return student_list_learn



def search_subject_id_by_student_id(student_id):
    for subject in subjects:
        for student in subject.student_list:
            if student.student_id == student_id:
                return subject.subject_name


print(search_students_by_teacher_id("10"))
print("--------------------------------")
print(search_students_by_teacher_id("20"))
print("--------------------------------")
print(search_subject_id_by_student_id("66010004"))
print("--------------------------------")

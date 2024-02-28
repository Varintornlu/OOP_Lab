#สร้างคลาส Student ที่มี attributesทุกตัวเป็น private
class Student:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
    
    def get_student_id(self):
        return self.__student_id
    
    def get_student_name(self):
        return self.__student_name
    
#สร้างคลาส Subject ที่มี attributesทุกตัวเป็น private
class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__credit = credit

    def get_subject_id(self):
        return self.__subject_id
    
    def get_subject_name(self):
        return self.__subject_name
    
    def get_credit(self):
        return self.__credit

    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def get_teacher(self):
        return self.__teacher

#สร้างคลาส Teacher ที่มี attributesทุกตัวเป็น private
class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name

    def get_teacher_id(self):
        return self.__teacher_id

    def get_teacher_name(self):
        return self.__teacher_name

#สร้างคลาส Enrollment ที่มี attributesทุกตัวเป็น private
class Enrollment:
    def __init__(self, student, subject, grade = None):
        self.__student = student
        self.__subject = subject
        self.__grade = grade

    def get_student(self):
        return self.__student
    
    def get_subject(self):
        return self.__subject
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        self.__grade = grade

#สร้างlistว่าง
student_list = []     
subject_list = []
teacher_list = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id):
    #ลูปใน subject_list เทียบหาวิชาที่รหัสวิชาตรงกันแล้ว return object ออกมา
    for subject in subject_list:
        if subject.get_subject_id() == subject_id:
            return subject
    return None

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id):
    #ลูปใน student_list เทียบหารหัสนักเรียนที่ตรงกันแล้ว return object ออกมา
    for student in student_id:
        if student.get_student_id() == student_id:
            return student
    return None

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student, subject):
    #ถ้า student และ subject เป็น instance ให้ลูป object ใน enrollment_list ถ้าไม่เป็น instance จะให้return Error ออกมา
    if isinstance(student, Student) and isinstance(subject, Subject):
        for enrollment in enrollment_list:
            #ถ้าในลิสมี object student และ subject นั้นแล้วให้คืนค่า 'Alreagy Enrolled' ถ้ายังไม่มีให้เพิ่ม object student และ subject นั้นในลิสและจะให้return Done ออกมา
            if student == enrollment.get_student() and subject == enrollment.get_subject():
                return "Already Enrolled"
        enrollment_list.append(Enrollment(student, subject))
        return "Done"
    else:
        return "Error"


# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student, subject):
    #ถ้า student และ subject ไม่เป็น instance จะให้return Error ออกมา
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    #ถ้า student และ subject เป็น instance ให้เข้าลูป enrollment_list
    for enrollment in enrollment_list:
        #ถ้ามีobject studentและsubjectในลิส ให้ลบออก
        if enrollment.get_student() == student and enrollment.get_subject() == subject:
            enrollment_list.remove(enrollment)
            return "Done"
    #ถ้าไม่มีให้return Not Found ออกมา
    return "Not Found"

# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject, student):
    #ถ้าพบว่ามีการลงทะเบียนที่ตรงตามเงื่อนไขจะreturn object enrollmentออกมา ถ้าไม่พบการลงทะเบียนที่ตรงตามเงื่อนไขจะให้return Not Found ออกมา
    for enrollment in enrollment_list:
        if enrollment.get_subject() == subject and enrollment.get_student() == student:
            return enrollment
    return "Not Found"

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject):
    #สร้างลิสว่าง
    enrollment_student = []
    #ลูปใน enrollment_list ตรวจว่านักศึกษาลงทะเบียนในรายวิชาที่กำหนดไหม ถ้ามีให้เพิ่ม instance ลงในลิสต์ enrollment_student
    for enrollment in enrollment_list:
        if enrollment.get_subject() == subject:
            enrollment_student.append(enrollment)
    return enrollment_student

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student):
    #สร้างลิสว่าง
    enrollment_subject = []
    #ลูปใน enrollment_list ตรวจว่านักศึกษาที่ลงทะเบียวิชานี้ตรงกับนักศึกษาที่ต้องการหาไหม ถ้าตรงให้เพิ่ม instance ลงในลิสต์ enrollment_student
    for enrollment in enrollment_list:
        if enrollment.get_student() == student:
            enrollment_subject.append(enrollment)
    #ถ้าจำนวนวิชาที่นักศึกษาลงน้อยกว่าเท่ากับ 0 ให้return Not Found ออกมา นอกจากนั้นให้return enrollment_subject
    if len(enrollment_subject) <= 0:
        return "Not Found"
    else:
        return enrollment_subject

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade):
    #ถ้าstudent และ subject เป็น instance และ เกรดเป็นตัวอักษร นอกเหนือจากนี้ให้return Error
    if isinstance(student, Student) and isinstance(subject, Subject) and grade.isalpha():
        enrollment = search_enrollment_subject_student(subject, student)
        #ถ้าไม่พบการลงทะเบียน ให้return  Not Found
        if enrollment is None:
            return "Not Found"
        #ถ้าไม่มีเกรดให้เพิ่มเกรดแล้วreturn Done แต่ถ้ามีเกรดอยู่แล้วให้return Error
        if enrollment.get_grade() is None:
            enrollment.set_grade(grade)
            return "Done"
        else:
            return "Error"
    else:
        return "Error"

# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search):
    #ลูปใน subject_list ถ้าพบวิชาที่ตรง จะreturnค่าชื่อครูผู้สอนของวิชานั้นๆกลับ ถ้าไม่พบวิชาที่ตรง จะreturnค่า Not Found ออกมา
    for subject in subject_list:
        if subject == subject_search:
            return subject.get_teacher()
    return "Not Found"

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject):
    #กำหนดตัวแปร
    count = 0
    #ลูปใน enrollment_list
    for enrollment in enrollment_list:
        #ตรวจสอบว่ารายวิชาตรงกับที่กำลังค้นหาไหม ถ้ามีเพิ่มจำนวนนักศึกษาที่ลงทะเบียน
        if enrollment.get_subject() == subject:
            count += 1
    # return จำนวนนักศึกษาที่ลงทะเบียนวิชานั้น
    if count > 0:
        return count
    else:
        return "Not Found"


# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student):
    #สร้างตัวแปร record เป็น dict เก็บข้อมูลการลงทะเบียนและผลการเรียนของนักศึกษา
    record = {}
    #ลูปใน enrollment_list
    for enrollment in enrollment_list:
        #ตรวจสอบว่านักศึกษาตรงกับที่กำลังค้นหาไหม ถ้าตรงเพิ่มข้อมูลการลงทะเบียนและผลการเรียนของนักศึกษาในrecord
        if enrollment.get_student() == student and enrollment.get_grade is not None:
            record[enrollment.get_subject().get_subject_id()] = [enrollment.get_subject().get_subject_name(), enrollment.get_grade()]
    #returnค่า recordกลับ
    return record

# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student):
    #กำหนดตัวแปร
    total_credit = 0
    total_weighted_grades = 0
    #ลูปใน enrollment_list ถ้านักเรียนตรงกับที่กำหนดไว้และมีเกรด จะทำการคำนวณtotal_credit และคูณกับtotal_weighted_grades โดยใช้ฟังก์ชัน grade_to_count เพื่อคิดเกรด 
    for enrollment in enrollment_list:
        if enrollment.get_student() == student and enrollment.get_grade() is not None:
            total_credit += enrollment.get_subject().get_credit()
            total_weighted_grades += grade_to_count(enrollment.get_grade()) * enrollment.get_subject().get_credit()
    #ถ้าหน่วยกิจรวมเป็น 0 returnค่า 0.0 กลับ
    if total_credit == 0:
        return 0.0
    return total_weighted_grades / total_credit


# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list:
        student_dict[enrollment.get_student().get_student_id()] = enrollment.get_student().get_student_name()
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = self.search_subject_that_student_enrolled(student) #มีselfหรือไม่มีก็ได้
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.get_subject().get_subject_id()] = enrollment.get_subject().get_subject_name()
    return subject_dict


#######################################################################################

#สร้าง instance พื้นฐาน
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103


create_instance()
register()

### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].get_subject_id()))
print("")

### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.get_student().get_student_id() for i in lst])
print("")

### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.get_subject().get_subject_id() for i in lst])
print("")

### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]).get_teacher_name())
print("")

### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(enroll.get_subject().get_subject_id(),enroll.get_student().get_student_id())
print("")

### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print(get_student_GPS(student_list[1])) 
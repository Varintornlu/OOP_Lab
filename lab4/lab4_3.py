class Student:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.student_mentor = None

students = []
students.append(Student('66010001', 'John'))
students.append(Student('65010001', 'Peter'))
students.append(Student('64010001', 'Tom'))
students.append(Student('63010001', 'Mary'))

students.append(Student('66010002', 'Jack'))
students.append(Student('65010002', 'James'))
students.append(Student('64010002', 'Lily'))
students.append(Student('63010002', 'Rose'))

students[0].student_mentor = students[1]
students[1].student_mentor = students[2]
students[2].student_mentor = students[3]

students[4].student_mentor = students[5]
students[5].student_mentor = students[6]
students[6].student_mentor = students[7]

def all_mentors(student_id, students):
  mentor_name_list = []
  """
   for student in students: #เช็คว่านักเรียนคนนี้มีพี่รหัสหรือไม่ ถ้ามีให้ใส่ชื่อพี่รหัสใน list
    if student.id == student_id and student.student_mentor != '':
      mentor_name_list.append(student.student_mentor.name)
      
  for student in students: #เช็คว่านักเรียนชื่อตรงกับพี่รหัสหรือไม่ ถ้าตรงก็เอาชื่อพี่รหัสของนักเรียนมาใส่ list ต่อแล้วก็เอาไปเช็คต่อ
    if student.name in mentor_name_list and student.student_mentor != '':
      mentor_name_list.append(student.student_mentor.name)
      
  """
  for student in students:
    if student.id == student_id:
      curr = student.student_mentor
  while curr != None :
    mentor_name_list.append(curr.name)
    curr = curr.student_mentor
  return mentor_name_list

def show_mentors(student_id):
  mentor_new = []
  if all_mentors(student_id,students) != []:
    for student in students:
      if student.name in all_mentors(student_id,students):
        mentor_new.append(student.id + ' ' + student.name)
    return mentor_new
  else:
    return ("No mentors")

def check_mentor(student_id_x, student_id_y): #เอาคนที่รหัสมากกว่า(เป็นรุ่นน้อง)มาหาlistพี่รหัส แล้วเช็คต่อว่ามีนักเรียนอีกคนในlistมั้ย
    if int(student_id_x) < int(student_id_y):
      for student in students:
        if student.id == student_id_x:
          return (student.name in all_mentors(student_id_y,students))
    else:
      for student in students:
        if student.id == student_id_y:
          return(student.name in all_mentors(student_id_x,students))

print(show_mentors('66010001'))
print(check_mentor('66010001', '65010001'))
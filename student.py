class basic :
    def __init__(self, name, ID, DOB):
        self.name = name
        self.id = ID
        self.DOB = DOB
    def print_id(self):
        print(self.id)

class student(basic):
    def __init__(self, name, ID, DOB, SID, grade1, grade2, grade3):
        super().__init__(name, ID, DOB)
        self.SID = SID
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
    def average(self):
        avg = (int(self.grade1) + int(self.grade2) + int(self.grade3))/3
        print(avg)
        
        
y = 0
names = []
ID = []
DOB = []
SID = []
grade1 = []
grade2 = []
grade3 = []
sorted_order = []
sorted_version = []
fp = open("student.txt", "r+")
student_raw = fp.read()
print (student_raw)
student_info = student_raw.split()
for x in range(len(student_info)):
    n = x % 7
    if n == 0:
        names.append(student_info[x])
    if n == 1:
        ID.append(student_info[x])
    if n == 2:
        DOB.append(student_info[x])
    if n == 3:
        SID.append(student_info[x])
    if n == 4:
        grade1.append(student_info[x])
    if n == 5:
        grade2.append(student_info[x])
    if n == 6:
        grade3.append(student_info[x])

student1 = student(names[0], ID[0], DOB[0], SID[0], grade1[0], grade2[0], grade3[0])
student2 = student(names[1], ID[1], DOB[1], SID[1], grade1[1], grade2[1], grade3[1])
student3 = student(names[2], ID[2], DOB[2], SID[2], grade1[2], grade2[2], grade3[2])
student4 = student(names[3], ID[3], DOB[3], SID[3], grade1[3], grade2[3], grade3[3])
student5 = student(names[4], ID[4], DOB[4], SID[4], grade1[4], grade2[4], grade3[4])
print("id of student1 is")
student1.print_id()
print("student1 info is\n", student1.__dict__)
print("student2 info is\n", student2.__dict__)
print("gpa for student1 is")
student1.average()
for x in grade2:
    y = int(x) + y
avg = y/5
print("avg of grade2 is" ,avg)
#finding the sorted version index order
sorted_order = sorted(range(len(grade2)), key=lambda k: grade2[k])
for x in range(5):
    sorted_version.append(names[sorted_order[x]])
    sorted_version.append(" ")
    sorted_version.append(ID[sorted_order[x]])
    sorted_version.append(" ")
    sorted_version.append(DOB[sorted_order[x]])
    sorted_version.append(" ")
    sorted_version.append(SID[sorted_order[x]])
    sorted_version.append(" ")
    sorted_version.append(grade1[sorted_order[x]])
    sorted_version.append(" ")
    sorted_version.append(grade2[sorted_order[x]])
    sorted_version.append(" ")
    sorted_version.append(grade3[sorted_order[x]])
    sorted_version.append("\n")
sorted_version_str = ' '.join(sorted_version)
print(sorted_version_str)
fp.write(sorted_version_str)
fp.close()
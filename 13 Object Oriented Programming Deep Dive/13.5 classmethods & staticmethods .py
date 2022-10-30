import math


class Student:
    numberOfStudents = 0
    scholarship_increment = 1.10

    def __init__(self, fname, lname, id, FatherName, scholarship):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.FatherName = FatherName
        self.scholarship = scholarship

        Student.numberOfStudents += 1

    def __str__(self):
        return f'{self.id} {self.fname} {self.lname} {self.FatherName} {self.scholarship}'
    '''def __str__(self):
        return f'ID: {self.id}\nFull Name: {self.fname} {self.lname}\nFather Name: {self.FatherName}\nCurrent Scholarship: {self.scholarship}\nNext year your Scholarship will be Increased by,\nAnnual Increment: {str(math.floor((Student.scholarship_increment*100)-100))}%  \nScholarship: {self.scholarship*self.scholarship_increment}'''

    @classmethod
    def set_scholarship_increment(cls, increment):
        cls.scholarship_increment = increment

    @classmethod
    def from_string(cls, std_str):
        # fname, lname, id, FatherName, scholarship
        fname, lname, id, FatherName, scholarship = std_str.split('-')
        return cls(fname, lname, id, FatherName, scholarship)


Student.set_scholarship_increment(1.20)

std1 = Student('Farhan', 'Qadir', 5562, 'Abdul Qadir', 10000)
print(std1)
print()

std11 = 'Farhan-Qadir-5562-Abdul Qadir-10000'
print(std11)
print()

str_std1 = Student.from_string(std11)
print(str_std1)
'''std2 = Student()  # 'Haris', 'Zuberi', 6652, 'Waris Zuberi', 15000)
print(std2)
print()'''


'''std3 = Student('bilal', 'adil', 6655, 'Waris Zuberi', 18000)
print(std3)
print()
std4 = Student('amin', 'Zuberi', 6653, 'Waris Zuberi', 20000)
print(std4)
print()
std5 = Student('alwaz', 'akram', 6649, 'Waris Zuberi', 25000)
print(std5)
print()'''

print(Student.numberOfStudents)

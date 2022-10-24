# ====================== Classes & Instances ===================

'''class Student:
    pass


std1 = Student()
std2 = Student()
std3 = Student()

print(std1)
print(std2)
print(std3)

std1.fname = 'Haris'
std1.lname = 'Zuberi'
std1.id = '0001'
std1.FatherName = 'Waris Zuberi'

std2.fname = 'Amin'
std2.lname = 'Ahmed'
std2.id = '0002'
std2.FatherName = 'Waris Zuberi'

std3.fname = 'Bilal'
std3.lname = 'Adil'
std3.id = '0003'
std3.FatherName = 'Adil Zuberi'

print(std1.fname, std1.lname, std1.id, std1.FatherName)
print(std2.fname, std2.lname, std2.id, std2.FatherName)
print(std3.fname, std3.lname, std3.id, std3.FatherName)'''


class Student:
    def __init__(self, fname, lname, id, FatherName):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.FatherName = FatherName

    def __str__(self):
        return f'ID: {self.id}\nFull Name: {self.fname} {self.lname}\nFather Name: {self.FatherName}'


std1 = Student('Haris', 'Zuberi', '0001', 'Waris Zuberi')
std2 = Student('Amin', 'Zuberi', '0002', 'Waris Zuberi')
std3 = Student('Bilal', 'Adil', '0003', 'Adil Zuberi')
print(std1.id, std1.fname, std1.lname, std1.FatherName)
print(std2.id, std2.fname, std2.lname, std2.FatherName)
print(std3.id, std3.fname, std3.lname, std3.FatherName)
print()
print(std1)
print()
print(std2)
print()
print(std3)
print()

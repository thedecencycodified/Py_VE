

import math


class Student:
    scholarship_increment = 1.10

    def __init__(self, fname, lname, id, FatherName, scholarship):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.FatherName = FatherName
        self.scholarship = scholarship

    def __str__(self):
        return f'ID: {self.id}\nFull Name: {self.fname} {self.lname}\nFather Name: {self.FatherName}\nCurrent Scholarship: {self.scholarship}\nNext year your Scholarship will be Increased by,\nAnnual Increment: {str(math.floor((Student.scholarship_increment*100)-100))}%  \nScholarship: {self.scholarship*self.scholarship_increment}'

    '''def FormattedNames(self):
        return f'{self.id} {self.fname} {self.lname} son of {self.FatherName}'''


std1 = Student('Farhan', 'Qadir', 5562, 'Abdul Qadir', 10000)
std2 = Student('Haris', 'Zuberi', 6652, 'Waris Zuberi', 15000)

print(std1)
print(std2)
'''annual_increment = str(math.floor((Student.scholarship_increment*100)-100))+'%'
print(annual_increment)'''

'''print(std1)
print(std1.id)
print(std1.fname)
print(std1.FormattedNames)
print(std1.FormattedNames())
student1 = std1.FormattedNames()
print(student1)'''


'''print(f'Id: {std1.id}')
print('First Name: '+std1.fname)
print('Last Name: '+std1.lname)
print('Father Name: '+std1.FatherName)

print(f'Id: {std2.id}')
print('First Name: '+std2.fname)
print('Last Name: '+std2.lname)
print('Father Name: '+std2.FatherName)'''

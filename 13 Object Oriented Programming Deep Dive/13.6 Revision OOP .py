# ============================ OOP Revision ========================\
import datetime
import math


class Employee:
    numberOfEmployees = 0
    salary_increment = 1.10

    def __init__(self, first_name, last_name, salary, middle_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.middle_name = middle_name

        Employee.numberOfEmployees += 1

    def __str__(self):
        if self.middle_name != '':
            return f'First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\nSalary: {self.salary}\nAnnual Salary Increment: {math.floor((self.salary_increment*100)-100)}%\nNext Year Your Salary Will Be,\nNew Salary: {math.floor(self.salary*self.salary_increment)}'
        else:
            return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nSalary: {self.salary}\nAnnual Salary Increment: {math.floor((self.salary_increment*100)-100)}%\nNext Year Your Salary Will Be,\nNew Salary: {math.floor(self.salary*self.salary_increment)}'

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary, middle_name = emp_str.split('-')
        return cls(first_name, last_name, salary, middle_name)

# regularmethods self
# classmethod cls
# staticmethod
# monday 0
# SUNDAY 6

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return f'It\'s Your Holiday!!'
        return f'Its Your Working Day'


emp1 = Employee('Muhammad', 'Taimoor', 100000, 'Salahuddin')
emp2 = Employee('Azam', 'Shaheed', 120000)
emp3 = Employee('Haris', 'Zuberi', 150000, 'Ahmed')
emp4 = 'Amin-Zuberi-160000-Ahmed'
'''emp4_str = Employee.from_string(emp4)
print(emp4_str)'''
print()
print(emp1)
print()
print(emp2)
print()
print(emp3)
print()
print(f'Total Employees: {Employee.numberOfEmployees}')


my_date = datetime.date(2022, 11, 3)
print(Employee.is_workingday(my_date))

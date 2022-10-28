# ================= Object Oriented Programming =========================
# ====================== Classes ============================
'''print(type('abc'))
print(type(55))
print(type(['abc']))
print(type(('abc', 12)))
print(type({'abc': 12}))
def func():
    pass
print(type(func))'''


'''class MyClass:  # creating class
    x = 10


obj = MyClass()  # creating object
print(obj.x)'''

# the __init__() Function


'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('Farhan', 27)

print(person.name, person.age)
print(person.age)'''


# the __str__() Function.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name} \nAge: {self.age}'


person = Person('Farhan', 27)

# print(person.name, person.age)
# print(person.age)
print(person)

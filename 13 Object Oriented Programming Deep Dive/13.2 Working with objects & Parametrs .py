# ================== Object Methods ====================
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name} \nAge: {self.age}'

    def myFunc(self):
        print('Hello your name is: ' + self.name)


man = Person('Farhan', 27)

# print(man.name, man.age)
# print(man.age)
print(man)
man.myFunc()
print(man.name)
man.name'''
# ======================== self parameter ==============================


'''class Person:
    def __init__(myChoice, name, age):
        myChoice.name = name
        myChoice.age = age

    def __str__(myChoice):
        return f'Name: {myChoice.name} \nAge: {myChoice.age}'

    def myFunc(myChoice):
        print('Hello your name is: ' + myChoice.name)


man = Person('Farhan', 27)

# print(man.name, man.age)
# print(man.age)
print(man)
man.myFunc()
print(man.name)
man.name'''

# ======================== modifying objects ==============================


'''class Person:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name} \nAge: {self.age}'

    def myFunc(self):
        print('Hello your name is: ' + self.name)


man = Person('Farhan')
print(man)
man.age = 50
print(man)

del man.age

# print(man)

del man
print(man)
'''


class MyClass:
    pass


print('Program has been executed!')

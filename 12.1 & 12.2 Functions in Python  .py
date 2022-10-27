# ===================== Functions =======================
'''def new_Funct():
    pass


print(new_Funct)
print(new_Funct())
new_Funct()'''


'''def new_Funct1():
    print('Function has been executed!!')


print(new_Funct1)
new_Funct1()
print(new_Funct1())'''


'''def myFunc():  # creating/defining a fuction
    print('Its a Function!!')


myFunc()  # calling a function
'''


'''def func(car):  # car is the required positional argument in the function
    print(car + ' is my favorite car!!')


func('BMW')'''


'''def add(a, b): # arguments
    print(a + b)


add(55, 66)
add('55', '66')'''


'''def add(a=5, b=6):  # parameters
    print(a * b)


add()
add(9, 7)
'''

# number of arguments
'''def name(fname='N/A', mname='N/A', lname='N/A', education='N/A'):
    print(
        f'welcome {fname} {mname} {lname}, your qualification is {education}!!!')


name()
name('S M', 'Farhan', 'Qadir', 'Professional Programmer')'''

# Arbitrary Arguments, *args (Tuple)


'''def ArbitraryArg(*Classmates):  # if the number of args are unknown we use *
    print('The Smartest classmate is ' + Classmates[2])


ArbitraryArg('Haris', 'Bilal', 'Amin', 'Sami')'''


'''def keywordArg(mate1, mate2, mate3, mate4):
    print('The Smartest boy is ' + mate3)


keywordArg(mate1='Haris', mate2='Bilal', mate3='Amin', mate4='Sami')'''

# Arbitrary Keyword Arguments, **kwargs (Dictionary)


'''def myCars(**cars):
    print('The 1st Best car is ' + cars['car3'])
    print('The 2nd Best car is ' + cars['car2'])
    print('The 3rd Best car is ' + cars['car1'])


myCars(car1='BMW', car2='Audi', car3='Toyota')'''


'''cars = ['BMW', 'Audi', 'Toyota']


def myCars(CARS):
    for car in CARS:
        print(car)


myCars(cars)'''

# Return


'''def func(arg):
    return 5*arg


func(55)
func('Ali ')
print(func(77))
print(func('Ali '))'''

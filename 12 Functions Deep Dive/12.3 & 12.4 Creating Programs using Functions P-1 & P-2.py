'''def greeting(user):
    print(f'Welcome, {user.title()}')


greeting('farhan qadir')'''

# ----------------------------------------------------------


'''def names(fname, lname, mname=''):
    if mname:
        Full_Name = f'{fname} {mname} {lname}'
    else:
        Full_Name = f'{fname} {lname}'
    return Full_Name.title()


name = names('farhan', 'shah')
print(name)
name = names('farhan', 'shah', 'qadir')
print(name)'''

# ----------------------------------------------------------


'''def persons(fname, lname, age=None):
    person = {'fname': fname, 'lname': lname}
    if age:
        person['age'] = age
    return person


personBio = persons('Farhan', 'Qadir', age=27)
print(personBio)'''

# ----------------------------------------------------------


'''def names(fname, lname):
    full_name = f'{fname} {lname}'
    return full_name.title()


while True:
    print('\nType \'q\' to quit the program!')
    print('please provide following credencials,')
    f_name = input('First Name: ')
    if f_name == 'q':
        break
    l_name = input('Last Name: ')
    if f_name == 'q':
        break

    name = names(f_name, l_name)
    print(f'\nWelcome, {name}!\n')'''

# ----------------------------------------------------------


'''def greeting(names):
    for name in names:
        message = f'Hello, {name.title()}!'
        print(message)


userNames = ['haris', 'bilal', 'amin']
greeting(userNames)'''

# ----------------------------------------------------------


'''def profile(fname, lname, **moreInfo):
    moreInfo['First Name'] = fname
    moreInfo['Last Name'] = lname
    return moreInfo


userProfile = profile('Farhan', 'Qadir', ID='12346',
                      Field='Programming', interest='Python')
print(userProfile)'''

# ----------------------------------------------------------


'''def polling(age):
    if age <= 0:
        print('Please Review Your Credentials!')
    elif age > 0 and age <= 17:
        print('You Are Not Eligible For Voting!')
    elif age >= 18 and age <= 100:
        print('You Are Eligible For Voting!')
    else:
        print('You Are Senior Citizen, We Respect You, You Must Take Rest!')


Age = int(input('Please Enter Your Age: '))
polling(Age)'''

# ----------------------------------------------------------
# factortial
# n! = n x (n-1) x (n-2) x (n-3) x (n-4) x (n-5).....1
# n! = n x (n-1)!
# 6! = 6 x (6-1) x (6-2) x (6-3) x (6-4) x (6-5)
# 6! = 6 x 5 x 4 x 3 x 2 x 1
# 6! = 720


def factorialFunc(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n+1):
        product *= i
        #product = product * i
    return product


for n in range(1, 6):
    print(n, factorialFunc(n))

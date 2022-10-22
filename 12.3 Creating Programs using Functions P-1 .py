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

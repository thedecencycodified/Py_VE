# ================= While Loop =========================
'''number = 0
while number < 10:
    print(number)
    number = number + 1'''

'''number = 0  # break statement in while loop
while number < 10:
    print(number)
    if number == 5:
        break
    number = number + 1'''

'''number = 0  # continue statement in while loop
while number < 10:
    number = number + 1
    if number == 7:
        continue
    print(number)'''

'''number = 0  # else statement with while loop
while number < 10:
    print(number)
    number = number + 1
else:
    print('The Program has been Executed!!')'''

# ========================== While Loop Programs ==========================
'''import random
myNumber = -5
while myNumber <= 10:
    print(myNumber)
#    myNumber = myNumber + 1
    myNumber += 1
'''
# =======================================================
'''task = 'Tell me Something, & I will repeat it back to you: '
task += '\nEnter \'exit\' if you want to end the program.'
message = ''

while message != 'exit':
    message = input(task)
    print(message)'''

# =======================================================
'''task = '\nEnter \'exit\' if you want to end the program. '
task += '\nTell me Something, & I will repeat it back to you: '
active = True
while active:
    message = input(task)
    if message == 'exit':
        active = False
    else:
        print(message)'''

# =======================================================
'''task = '\nEnter \'exit\' if you want to end the program. '
task += '\nTell me your favorite food: '
while True:
    food = input(task)
    if food == 'exit':
        break
    else:
        print(f'I\'d Love to eat {food}!')'''

# =======================================================
'''unconfirmed_users = ['haris', 'amin', 'bilal', 'farhan', 'sami']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)
    print('\nFollowing users have been confirmed!\n')
    print(confirmed_users)
    print(unconfirmed_users)'''

# =======================================================

'''responses = {}
polling_active = True
while polling_active:
    print('If you want to end the program then write \'exit\'!')
    name = input('\nWhat is your Name: ')
    Response = input('To Which Political Party do you want to cast a Vote? ')
    responses[name] = Response
    if name == 'exit':
        polling_active = False
print(
    f'\n===================\nPolling Result\n===================\n{responses}\n====================')'''

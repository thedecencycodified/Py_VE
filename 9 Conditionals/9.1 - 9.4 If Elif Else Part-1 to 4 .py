# ============== Comparisons Operators =================
# Equal to                  : ==
# Not Equals to             : !=
# Greater Than              : >
# Less Than                 : <
# Greater Than or Equals to : >=
# Less than or Equals to    : <=
# Logical operators and, or , not, in, not in, is, is not

# if True:
#     print('Hello World!')
# if False:
#     print('Hello User!')
#
# a = True
# if a:
#     print('Hi')


# ====================== Short hand if else ===============
'''a = 15
b = 16
if a > b:
    print('Yes you are right!!')

print('Yes you are also right') if a > b else print('You are wrong!!')'''
##########################################################
'''country = input('Services by The Decency Codified \nEnter Your Country Name: ')
if country == 'Pakistan' or country == 'pakistan' or country == 'PAKISTAN':
    print('Yes Our services are available in Pakistan!!')
elif country == 'India' or country == 'india' or country == 'INDIA':
    print('Yes Our services are available in India!!')
elif country == 'USA' or country == 'usa' or country == 'United States':
    print('Yes Our services are available in USA!!')
else:
    print('Sorry! Our services are NOT available in Your Country!!')'''

##########################################################
'''age = int(input('Enter Your Age: '))
if age < 0:
    print('It\'s Impossible, Please Enter you Proper Age!!')
elif age < 11:
    print('You are too small to be in programming and casting vote!!')
elif age < 18:
    print('You can be in programming But can\'t cast a vote!!')
elif age >= 18 and age <= 100:
    print('You can be in programming as well as you can cast a vote!!')
else:
    print('We respect your presence but you need to get rest!!')'''

##############################################################
# x = int(input('Enter the number x: '))
# y = int(input('Enter the number y: '))
# z = int(input('Enter the number z: '))
# maximum_number = max((x, y, z))
# print(maximum_number)


'''a = float(input('Enter the number a: '))
b = float(input('Enter the number b: '))
c = float(input('Enter the number c: '))
if a > b and a > c:
    maximum_Num = a
elif b > a and b > c:
    maximum_Num = b
else:
    maximum_Num = c
print('The Maximum Number is: ' + str(maximum_Num) + '(Concatenation)')
print('The Maximum Number is: {} (.format())'.format(maximum_Num))
print('The Maximum Number is: %s (percentage s)' % (maximum_Num))
print(f'The Maximum Number is: {maximum_Num} (f\'\')')'''

##################################################################
'''smartphones = ['apple', 'samsung', 'oppo', 'vivo', 'mi']
for mobiles in smartphones:
    if mobiles == 'apple' or mobiles == 'mi':
        print(mobiles.upper())
    else:
        print(mobiles.title())'''

##################################################################
'''pizza_topping = input('Which Topping On Pizza? ')
requested_topping = ['mushrooms', 'extra cheese', 'pepperoni']
if pizza_topping == 'mushrooms' in requested_topping:
    print('Adding Mushrooms...')
    print('Finished Making Your Desired Pizza!!!')
elif pizza_topping == 'pepperoni' in requested_topping:
    print('Adding pepperoni...')
    print('Finished Making Your Desired Pizza!!!')
elif pizza_topping == 'extra cheese' in requested_topping:
    print('Adding extra cheese...')
    print('Finished Making Your Desired Pizza!!!')
else:
    print('This Topping Is Not Available...')'''

##################################################################
'''available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

    print("\nFinished making your pizza!")'''

##################################################################
year = int(input("Which year? "))
if year % 4:
    # not divisible by 4
    print("no leap year")
elif year % 100 == 0 and year % 400 != 0:
    print("no leap year")
else:
    print("leap year")

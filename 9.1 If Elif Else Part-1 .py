# ============== Comparisons Operators =================
# Equal to                  : ==
# Not Equals to             : !=
# Greater Than              : >
# Less Than                 : <
# Greater Than or Equals to : >=
# Less than or Equals to    : <=

if True:
    print('You Are A Python Programmer')

if False:
    print('You Are A Python Programmer')

if True:
    print('Hello')

# ====================== if elif else  ======================
# a = int(input('Enter the number a: '))
# b = int(input('Enter the number b: '))
# if a > b:
#     print('a is greater than b')
# elif b > a:  # else if
#     print('b is greater than a')
# else:
#     print('both are equal')

# ====================== Short Hand If  ======================
a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
if a > b:
    print('a is greater than b')


# ====================== some programs ==============================
person = input("Nationality? ")
if person == "Paksitani":
    print("To Kesy Hain Ap Log? ")
#############################################
person = input("Nationality? ")
if person == "Pakistani" or person == "Muslim":
    print("Assalam Alaikum!!!")
#############################################
person = input("Nationality? ")
if person == "Arabic" or person == "Muslim":
    print("Marhaba Ya Habibi")
if person == "Pakistani" or person == "Muslim":
    print("To Kesy Hain Ap Log? ")
#############################################
person = input("Nationality? ")
if person == "Pakistani" or person == "Muslim":
    print("We love Pakistan!!!")
elif person == "Indian" or person == "Hindustani":
    print("Pakistan Will Conquer India InshaAllah?")
else:
    print("You are neither Pakistani nor Hindustani.")
    print("So, let us speak English!")
#############################################
age = int(input("Your Age: "))
print()
if age < 0:
    print("This cannot be true!")
elif age == 10:
    print("No One Exist of This Age in This Room!")
elif age == 13:
    print("This Is Cute Amin!")
elif age == 17:
    print("Yeah Boy, This Is Haris!")
elif age == 19:
    print("Masoom Boy Bilal!")
else:
    print("Ab To Farhan Hi Bacha Hai!!!")
#############################################
x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))
if x > y and x > z:
    maximum = x
elif y > x and y > z:
    maximum = y
else:
    maximum = z
print("The maximal value is: " + str(maximum))
#############################################
x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))
maximum = max((x, y, z))
print("The maximal value is: " + str(maximum))
#############################################
'''A leap year is a calendar year containing an additional day added to 
keep the calendar year synchronized with the astronomical or seasonal 
year. In the Gregorian calendar, each leap year has 366 days instead of 
365, by extending February to 29 days rather than the common 28. These 
extra days occur in years which are multiples of four (with the exception 
of centennial years not divisible by 400). Write a Python program, which 
asks for a year and calculates, if this year is a leap year or not.'''

year = int(input("Which year? "))
if year % 4:
    # not divisible by 4
    print("no leap year")
elif year % 100 == 0 and year % 400 != 0:
    print("no leap year")
else:
    print("leap year")
#################################################
'''Body mass index (BMI) is a value derived from the mass (weight) and height of a person. 
The BMI is defined as the body mass divided by the square of the body height, and is universally 
expressed in units of kg/m2, resulting from mass in kilograms and height in metres.
 Write a program, which asks for the length and the weight of a person and returns an 
 evaluation string according to the following table:
BMI Evaluation'''
height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

bmi = weight / height ** 2
print(bmi)
if bmi < 15:
    print("Very severely underweight")
elif bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal (healthy weight)")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese Class I (Moderately obese)")
elif bmi < 40:
    print("Obese Class II (Severely obese)")
else:
    print("Obese Class III (Very severely obese)")
################################################
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
##################################################
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"{user.title()}, you are NOT allowed to post any response.")
##################################################
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
##################################################
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
##################################################
toppings = input('Which topping on pizza? ')
requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
##################################################
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

    print("\nFinished making your pizza!")

# Formatting Strings in Python .format(), %s, f''

name = str(input('Enter Your Name: '))
percentage = str(input('Enter Your Percentage: '))
grade = str(input('Enter Your Grade: '))
print(name + ' You Got '+percentage+' percentage and Placed in Grade '+grade)

# .format()
print('{} You Got {}% and Placed in Grade {}'.format(name, percentage, grade))

# %s
print("%s You Achieved %s percent and Placed In Grade %s" %
      (name, percentage, grade))

# f''
print(f'{name} you got {percentage}% and placed in grade {grade}')

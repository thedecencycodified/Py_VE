# String Methods

#           012345678910
import numbers


greeting = 'Hello World'

# ============ count() ===========
print(greeting.count('Hello'))
print(greeting.count('World'))
print(greeting.count('H'))
print(greeting.count('o'))
print(greeting.count('l'))
print(greeting.count('wolrd'))
print(greeting.count('farhan'))

#           012345678910
greeting = 'Hello World'

# ============ upper() ===========
print(greeting.upper())

#           012345678910
greeting = 'Hello World'

# ============ lower() ===========
print(greeting.lower())

#           012345678910
greeting = 'hello world my name is farhan'

# ============ capitalize() ===========
print(greeting.capitalize())

#           012345678911234567892123
greeting = 'hello world my name is farhan'

# ============ find() ===========
print(greeting.find('farhan'))
print(greeting.find('hello'))
print(greeting.find('my'))

#           012345678911234567892123
greeting = 'hello world my name is farhan'

# ============ index() ===========
print(greeting.index('world'))
print(greeting.index('is'))
print(greeting.index('my'))

#           012345678911234567892123
greeting = 'hello world my name is farhan'

# ============ replace() ===========
print(greeting.replace('world', 'universe'))
print(greeting.replace('is', 'to'))
print(greeting.replace('my', 'your'))

#           012345
greeting = 'Galaxy is very big'
number = '45'

# ============ join() ===========
print('_'.join(greeting))
print('|'.join(greeting))
print('-'.join(greeting))
print(' - '.join(greeting))
print('+'.join(greeting))

print(greeting.isnumeric())
print(number.isnumeric())

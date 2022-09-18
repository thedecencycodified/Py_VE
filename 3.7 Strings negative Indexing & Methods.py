# ============== Negative Indexing ==============
#    01234 # normal indexing
#     ---- => 0 -4 -3 -2 -1
#             W  o  r  l  d
#    04321 # negative Indexing
# a = 'World'
# print(a)
# print(a[-1])
# print(a[-4])
# print(a[-3])
# print(a[-1:])
# print(a[-2:])
# print(a[-3:])
# print(a[-4:])
# print(a[0:])
# print(a[:-2])
# print(a[:-3])
# print(a[:-4])
# print(a[0:-1])
# print(a[-4:-2])

# ================== String Methods==============
# capitalize()	Converts the first character to upper case
a = 'my name is farhan'
print(a.capitalize())

# casefold()	Converts string into lower case
a = 'My NaMe'
print(a.casefold())

# center()	Returns a centered string
a = "farhan"
print(a.center(8))

# count()	Returns the number of times a specified value occurs in a string
a = 1, 2, 2, 2, 3, 4, 4
a = 'is is is is it it it'
print(a.count('is'))

# encode()	Returns an encoded version of the string

# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

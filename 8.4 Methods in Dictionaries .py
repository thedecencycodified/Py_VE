# ===================== Methods in Dictionaries ==========================
# my_Dict = { keys : Values }
myDict1 = {
    'Name': 'Farhan',
    'Age': 27,
    'P_Lang': 'Python',
    'Obtained_Marks': 540,
    'Total_Marks': 600,
    'Percentage': (540/600)*100,
    'Comment': 'You are Passed'
}
print(myDict1)

# ===================== copy() ==========================
newDict = myDict1.copy()
print(newDict)

# ===================== get() ==========================
print(myDict1.get('Age'))
print(myDict1.get('Comment'))

# ===================== items() ==========================
print(myDict1.items())

# ===================== keys() ==========================
print(myDict1.keys())

# ===================== values() ==========================
print(myDict1.values())

# ===================== update() ==========================
myDict1.update({'Grade': 'A'})
print(myDict1)

# ===================== pop() ==========================
myDict1.pop('P_Lang')
print(myDict1)

# ===================== popitem() ==========================
myDict1.popitem()
print(myDict1)

# ===================== fromkeys() ==========================
keys = ('a', 'b', 'c')
values = (5, 6, 4)
newDict2 = dict.fromkeys(keys, values)
print(newDict2)

# ===================== setdefault() ==========================
myDict1 = {
    'Name': None,
    'Age': 27,
    'P_Lang': 'Python',
    'Obtained_Marks': 540,
    'Total_Marks': 600,
    'Percentage': (540/600)*100,
    'Comment': 'You are Passed'
}
myDict1.setdefault('Names', 'Haris')
print(myDict1)


# ===================== clear() ==========================
myDict1.clear()
print(myDict1)

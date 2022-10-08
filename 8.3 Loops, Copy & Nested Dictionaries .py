# ===================== Loops in Dictionaries ==========================
# my_Dict = { keys : Values }
from email.headerregistry import Group


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

for itemKeys in myDict1:
    print(itemKeys)

for itemValues in myDict1:
    print(myDict1[itemValues])

for keys in myDict1.keys():
    print(keys)

for values in myDict1.values():
    print(values)

for items in myDict1.items():
    print(items)

# ===================== Copy Dictionaries ==========================
myDict1 = {
    'Name': 'Farhan',
    'Age': 27,
    'P_Lang': 'Python',
    'Obtained_Marks': 540,
    'Total_Marks': 600,
    'Percentage': (540/600)*100,
    'Comment': 'You are Passed'
}

newDict = myDict1.copy()
print(newDict)
print(myDict1)

newDict2 = dict(myDict1)
print(newDict2)

# ===================== Nested Dictionaries ==========================
Total_Groups = {
    'Group1': {
        'Sci_Sub1': 'Physics',
        'Sci_Sub2': 'Chemistry',
        'Sci_Sub3': 'Math'
    },
    'Group2': {
        'Sci_Sub1': 'Economics',
        'Sci_Sub2': 'Business Studies',
        'Sci_Sub3': 'Accounting'
    },
    'Group3': {
        'Sci_Sub1': 'Math',
        'Sci_Sub2': 'Computer Science',
        'Sci_Sub3': 'Programming'
    },
}
print(Total_Groups)
Group1 = {
    'Sci_Sub1': 'Physics',
    'Sci_Sub2': 'Chemistry',
    'Sci_Sub3': 'Math'
}
Group2 = {
    'Sci_Sub1': 'Economics',
    'Sci_Sub2': 'Business Studies',
    'Sci_Sub3': 'Accounting'
}
Group3 = {
    'Sci_Sub1': 'Math',
    'Sci_Sub2': 'Computer Science',
    'Sci_Sub3': 'Programming'
}

Total_Groups2 = {
    'Group1': Group1,
    'Group2': Group2,
    'Group3': Group3
}
print(Total_Groups2)

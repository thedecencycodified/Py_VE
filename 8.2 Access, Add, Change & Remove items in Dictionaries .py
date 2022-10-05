# ===================== Dictionaries in Python ==========================
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
# ================= Accessing Items =========================

print(myDict1['Name'])
print(myDict1['Total_Marks'])
print(myDict1['Comment'])

print(myDict1.get('P_Lang'))
print(myDict1.keys())
print(myDict1.values())

# ================= Add Items =========================
print(myDict1)
newItem = myDict1.keys()
print(newItem)
myDict1['School'] = 'Bahria College'
print(newItem)

# ================= Changing Items ===================
myDict1['Obtained_Marks'] = 500
myDict1['Total_Marks'] = 700
myDict1['Percentage'] = (500/700)*100
print(myDict1)

myDict1.update({'Subject': 'Computer Science'})
print(myDict1)

# ================= Removing Items ===================

myDict1.popitem()
print(myDict1)

myDict1.pop('School')
myDict1.pop('Age')
print(myDict1)

myDict1.clear()
print(myDict1)

del myDict1
print(myDict1)

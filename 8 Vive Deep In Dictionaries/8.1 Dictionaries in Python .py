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
print(myDict1)
print(myDict1['Name'])
print(myDict1['Percentage'])
print(myDict1['Comment'])
print(myDict1.keys())
print(myDict1.values())
print(len(myDict1))
print(type(myDict1))

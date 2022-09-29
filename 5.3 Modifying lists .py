# ================ Access items in the list =================
#         0         1       2  3  4  5
#         0        -5      -4 -3 -2 -1
list1 = ['farhan', 'haris', 1, 2, 3, 9.99]
print(list1[2])
print(list1[0])
print(list1[1])
print(list1[-5])
print(list1[-2])
print(list1[-1])

# =================== Changing items in the list =============
#         0         1           2       3       4       5
list2 = ['farhan', 'haris', 'bilal', 'amin', 'sami', 'ali']
print(list2)
list2[2] = 'hussain'
print(list2)
list2[1:4] = ['Amin', 'Sami', 'Ali']
print(list2)
list2[1:3] = ['Hassan']
print(list2)

# =================== Adding items in the list =============
list3 = ['Amin', 'Sami', 'Ali', 'Haris']
list4 = ['Farhan', 'Bilal', 'Kamran']
list3.append('Hassan')
print(list3)
list3.insert(0, 'Hussain')
print(list3)
list3.extend(list4)
print(list3)
myTuple = (1, 2, 3)
list3.extend(myTuple)
print(list3)

# =================== Removing items from the list =============
list5 = ['Amin', 'Sami', 'Ali', 'Haris', 'Farhan', 'Bilal', 'Kamran']

list5.remove('Farhan')
print(list5)

list5.pop()
print(list5)

list5.pop(2)
print(list5)

del list5[1]
print(list5)

list5.clear()
print(list5)

del list5
print(list5)

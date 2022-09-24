# ================= Lists in Python ================
# lists in python stores mulple values in a sigle variable
# list1 = ['Ali', 'Sami', 'Haris', 'Bilal', 'Amin']
# list2 = [1, 2, 3, 4, 4, 4, 5, 6]
# list3 = [5.5, 6.4, 9.8, 99.99]
# list4 = [5j, 12j, 99.9j]
# list5 = [True, False]
# list6 = []
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)
# print(list6)
# ================= Index to Item ===================
# +ve     0        1      2  3  4    5    6   7   8     9
# -ve     0       -9     -8 -7 -6   -5   -4  -3  -2    -1
list7 = ['Haris', 'Amin', 1, 2, 3.5, 6.9, 5j, 9j, True, False]
print(list7)
print(list7[9])
print(list7[5])
print(list7[-6])
print(list7[-9])
print(list7[0])
print(list7[:])  # [(strating point):(limit)] # indexing always less than limit
print(list7[5:])
print(list7[3:])
print(list7[-2:])
print(list7[-7:])
print(list7[:9])
print(list7[:4])
print(list7[:-5])
print(list7[:-9])
print(list7[1:6])
print(list7[4:8])
print(list7[-4:-2])
print(list7[-9:-3])

# =============== Item to Index ==================
print(list7.index('Haris'))
print(list7.index(9j))
print(list7.index(False))

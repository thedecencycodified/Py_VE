# ================== Accessing Tuples ================
#         0  1  2  3   4    5    6
#         0 -6 -5 -4  -3   -2   -1
tuple1 = (1, 2, 3, 4, 'A', 'B', 'C')
'''print(tuple1)
print(tuple1[5])
print(tuple1[-5])
print(tuple1[2:5])
print(tuple1[-5:-1])'''

# myInput = input('What do you want to find? ')
# if myInput in tuple1:
#     print('Yes this item exists')
# else:
#     print('No this item don\'t exists')

# ================== Updating Tuples ================
# tuples cant be changed or update but we can do this by changing tuple into the list using constructor
# list()
# tuple()
# set()
# dict()
tuple2 = ('Python', 'Java', 'C++', 'Javascript')
print(tuple2)
tuple2_to_list = list(tuple2)
tuple2_to_list.append('C#')
print(tuple2_to_list)
tuple2 = tuple(tuple2_to_list)
print(tuple2)

# ======================= Unpacking Tuples ======================
tuple3 = (1, 2, 3)  # packing
(a, b, c) = tuple3  # unpacking
print(a)
print(b)
print(c)
tuple3 = (1, 2, 3, 4, 5, 6, 7)  # packing
(a, b, c, *d) = tuple3  # unpacking
print(a)
print(b)
print(c)
print(d)

# ======================= Joining Tuples ======================
tuple4 = (1, 2, 3, 4, 5)
tuple5 = (6, 7, 8, 9)
joining_tuples = tuple4+tuple5
print(joining_tuples)
print(tuple4+tuple5)
print(tuple4*2+tuple5*3)

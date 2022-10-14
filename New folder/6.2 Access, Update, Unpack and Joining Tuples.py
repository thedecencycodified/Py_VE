# ================== Accessing Tuples ================
#         0  1  2  3   4    5    6
#         0 -6 -5 -4  -3   -2   -1
tuple1 = (1, 2, 3, 4, 'A', 'B', 'C')
print(tuple1)
print(tuple1[5])
print(tuple1[-5])
print(tuple1[2:5])
print(tuple1[-5:-1])

# myInput = input("What Do You Want To Find? ")
# if myInput in tuple1:
#     print('Yes this item exists')
# else:
#     print('This Item Does Not Exist')

# ================== Updating Tuples ================
# tuples cant be changed or update but we can do this by changing tuple into the list
tuple2 = ('Python', 'Java', 'C++', 'Javascript')
newChangeList = list(tuple2)
newChangeList.append('C#')
print(newChangeList)
tuple2 = tuple(newChangeList)
print(tuple2)

# ======================= Unpacking Tuples ======================
tuple3 = (1, 2, 3)  # packing
(a, b, c) = tuple3  # unpacking
print(a)
print(b)
print(c)
tuple3 = (1, 2, 3, 4, 5, 6)  # packing
(a, b, *c) = tuple3  # unpacking
print(a)
print(b)
print(c)

# ======================= Joining Tuples ======================
tuple4 = (1, 2, 3, 4, 5)
tuple5 = (1, 2, 3, 4, 5)
a = tuple4+tuple5
print(a)
print(tuple4+tuple5)
print(tuple4*2+tuple5*3)

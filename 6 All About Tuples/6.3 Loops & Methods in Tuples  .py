# ================== Loops in Tuples =================
tuple1 = ('a', 'b', 'c', 'd', 1, 2, 3, 4)
print(tuple1)
for items in tuple1:
    print(items)

for index in range(len(tuple1)):
    print(index)

for x in range(len(tuple1)):
    print(tuple1)

a = 0
while a < len(tuple1):
    print(tuple1)
    a = a + 1

b = 0
while b < len(tuple1):
    print(tuple1[b])
    b = b + 1

# ================== Methods in Tuples =================
tuple2 = (1, 1, 1, 'd', 2, 3, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 'a')
print(tuple2)
print(tuple2.count(4))
print(tuple2.count(1))
print(tuple2.count(99))
print(tuple2.index(5))
print(tuple2.index('a'))
print(tuple2.index('d'))

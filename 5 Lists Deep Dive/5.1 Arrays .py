# =============== Arrays ==============
# arrays are used for storing multiple values in a single variable
array1 = ['farhan', 'shahab', 'mehtab']
# array2 = [1, 2, 3, 4]
# array3 = [5.5, 6.7, 99.99]
# array4 = [5j, 99j]
# print(array1, array2, array3, array4, array5)
# print(array1, '\n', array2, '\n', array3, '\n', array4, '\n', array5)
# print(array1)
# print(array2)
# print(array3)
# print(array4)
#          0       1  2    3
array5 = ['Haris', 'Amin', 9.8, 7j]
print(array5)
print(array5[3])
print(array5[1])
print(array5[0])
array5[3] = 'Karachi'
print(array5)
print(len(array5))
array5.append('city')
print(array5)
array5.pop()
print(array5)
array5.pop(2)
print(array5)
array5.remove('Karachi')
print(array5)
array5.extend(array1)
print(array5)
array6 = array5.copy()
print(array6)
print(array5.count('Haris'))
print(array5.count('Sami'))
print(array5.index('farhan'))
array5.insert(4, 'Sami')
print(array5)
array5.reverse()
print(array5)
array5.sort()
print(array5)

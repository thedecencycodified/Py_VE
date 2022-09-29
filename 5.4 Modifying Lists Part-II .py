# ==================== Sorting Lists ========================
list1 = ['Amin', 'Sami', 'Ali', 'Haris', 'Farhan', 'Bilal', 'Kamran',
         'amin', 'sami', 'ali', 'haris', 'farhan', 'bilal', 'kamran']
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list2 = [5, 6, 8, 1, 6, 9, 7, 22, 3, 99]
print(list2)

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list1.reverse()
print(list1)

# ================== Copying list ===================
list3 = [1, 2, 3, 4, 'Bill']
print(list3)
list4 = list3.copy()
print(list4)

# ================ joining lists ====================
list5 = list3 + list4
print(list5)
list5.extend(list4)
print(list5)

print(list5.count(4))

# .append()
# .extend()
# .clear()
# .copy()
# .count()
# .index()
# .insert()
# .remove()
# .pop()
# .sort()
# .reverse()

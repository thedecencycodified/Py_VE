# ================== Formatting List ===================
list1 = ['Ali', 'Sami', 'Haris', 'Bilal', 'Amin']
list2 = [1, 2, 3, 4, 4, 4, 5, 6]
list3 = [5.5, 6.4, 9.8, 99.99]
list4 = [5j, 12j, 99.9j]
list5 = [True, False]

# print(list1, list2, list3, list4, list5)
# print(list1+list2+list3+list4+list5)
#
# print('{}{}{}{}{}'.format(list1, list2, list3, list4, list5))
# print('{}'.format(list1+list2+list3+list4+list5))
#
# print('%s%s%s%s%s' % (list1, list2, list3, list4, list5))
# print('%s' % (list1+list2+list3+list4+list5))
#
# print(f'{list1}{list2}{list3}{list4}{list5}')
# print(f'{list1+list2+list3+list4+list5}')

# ================= List Loops =======================
# list1 = ['Ali', 'Sami', 'Haris', 'Bilal', 'Amin']
# for items in list1:
#     print(items)
#
# list1 = ['Ali', 'Sami', 'Haris', 'Bilal', 'Amin']
# for index in range(len(list1)):
#     print(list1[index])
#     print(index)
#
# list1 = ['Ali', 'Sami', 'Haris', 'Bilal', 'Amin']
# x = 0
# while x < len(list1):
#     print(list1[x])
#     print(x)
#     x = x + 1

# ============= List Comprehension ===================
# list1 = ['Ali', 'Sami', 'Haris', 'Bilal', 'Amin']
# list7 = []
# for items in list1:
#     if 'Ali' in list1:
#         list7.append(items)
# print(list7)

# list1 = ['Ali', 'Sami', 'Haris', 'Bilal', 'Amin']
# list8 = [items for items in list1]
# print(list8)
# list9 = [items for items in list1 if 'Ali' in list1]
# print(list9)

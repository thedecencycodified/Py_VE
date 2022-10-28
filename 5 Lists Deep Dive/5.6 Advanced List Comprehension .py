# ==================== List Comprehensions ===================
my_string = 'Python'
my_List = [x for x in my_string]
print(my_List)

my_list_1 = ['ali', 'sami', 'adnan', 'amin', 'haris', 'bilal']
newList = []
for items in my_list_1:
    newList.append(items)
    print(items)
print(newList)

my_list_1 = ['ali', 'sami', 'adnan', 'amin', 'haris', 'bilal']
newList1 = [items for items in my_list_1]
print(newList1)

newList2 = [items for items in my_list_1]
print(newList2[2])

newList3 = [items for items in my_list_1 if 'farhan' in my_list_1]
print(newList3)

newList4 = [items for items in my_list_1 if 'haris' in my_list_1]
print(newList4)

even_list = [e for e in range(20) if e % 2 == 0]
print(even_list)

odd_list = [o for o in range(20) if o % 2 == 1]
print(odd_list)

prime_list = [p for p in range(2, 40) if all(p % y != 0 for y in range(2, p))]
print(prime_list)

my_list_2 = [a for a in range(5, 94) if a % 2 == 0 and a % 5 == 0]
print(my_list_2)

if_else_list = ['True' if x % 2 == 0 else 'False' for x in range(10)]
print(if_else_list)

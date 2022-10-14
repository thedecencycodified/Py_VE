my_string = 'Python'
myList = [x for x in my_string]
print(myList)

myList1 = ['ali', 'sami', 'adnan', 'amin', 'haris', 'bilal']

myList2 = [items for items in myList1]
print(myList2)


myList3 = [items for items in myList1]
print(myList3[2])

myList4 = [items for items in myList1 if 'sani' in myList1]
print(myList4)

even_list = [e for e in range(20) if e % 2 == 0]
print(even_list)

odd_list = [o for o in range(20) if o % 2 == 1]
print(odd_list)

prime_list = [p for p in range(2, 40) if all(p % y != 0 for y in range(2, p))]
print(prime_list)

my_list = [a for a in range(5, 92) if a % 2 == 0 and a % 5 == 0]
print(my_list)

if_else_list = ['True' if x % 2 == 0 else 'False' for x in range(10)]
print(if_else_list)

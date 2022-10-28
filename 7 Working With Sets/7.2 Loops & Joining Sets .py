# =================== Loops in Sets ==================
my_Set1 = {'Python', 'C++', 'Java', 'PHP', 'Javascript'}
print(my_Set1)

for items in my_Set1:
    print(items)

for items in range(len(my_Set1)):
    print(items)

for items in range(len(my_Set1)):
    print(my_Set1)

# =================== Joining in Sets ==================
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.update(set2)
print(set1)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

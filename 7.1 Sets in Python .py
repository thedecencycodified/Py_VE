# ===================== Sets in Python ======================
# the elements in sets does not repeat and duplicates are not allowed
my_Set1 = {'Python', 'C++', 'Java', 'PHP', 'Javascript'}
my_Set2 = {1, 2, 3, 4, 5, 6}
my_Set3 = {1.5, 2.9, 3.99, 4.0, 5.4, 6.3}
my_Set4 = {1j, 2j, 3j, 4j, 5j, 6j}
my_Set5 = {True, False}
my_Set6 = {True, 'Python', 2, 9.99, 8j}
print(my_Set1)
print(my_Set2)
print(my_Set3)
print(my_Set4)
print(my_Set5)
print(my_Set6)
# items in sets are unordered and unchangable
print(len(my_Set1))
print(len(my_Set2))
print(type(my_Set2))

# ================= Set Constructor =================
a = list()
b = tuple()
c = set()

# ================== Accessing items in the set =================
my_Set1 = {'Python', 'C++', 'Java', 'PHP', 'Javascript'}
print(my_Set1)
for items in my_Set1:
    print(items)

print('C++' in my_Set1)
print('C#' in my_Set1)
print('C#' not in my_Set1)

test = list(my_Set1)
print(test)
test.append('C#')
print(test)
my_Set1 = set(test)
print(my_Set1)

# ============== Adding, Updating , removing items & deleting sets ===================
my_Set1 = {'Python', 'C++', 'Java', 'PHP', 'Javascript'}
print(my_Set1)

my_Set1.add('CSS')
print(my_Set1)

my_Set1 = {'Python', 'C++', 'Java', 'PHP', 'Javascript'}
my_Set6 = {True, 'Python', 2, 9.99, 8j}
myList = [1, 2, 3]
mytuple = (4, 5, 6)

my_Set1.update(my_Set6)
print(my_Set1)

my_Set1.update(myList)
print(my_Set1)

my_Set1.update(mytuple)
print(my_Set1)

my_Set1 = {'Python', 'C++', 'Java', 'PHP', 'Javascript'}
my_Set1.remove('PHP')
print(my_Set1)

my_Set1.discard('Javascript')
print(my_Set1)

my_Set1.pop()
print(my_Set1)

my_Set1.clear()
print(my_Set1)

del my_Set1
print(my_Set1)

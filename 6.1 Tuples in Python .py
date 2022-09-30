# ============== Tuples ====================
list = ['Farhan', 1, 9.9]  # Mutable (it can be changed)
tuples = ('Farhan', 1, 9.9)  # Immutable (it cannot be changed)
my_tuple = ('Farhan', 'Shahab', 'Mehtab', 'Rehan',
            'Haris', 'Amin', 'Bilal', 'Mehtab')
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))
tuple1 = ('Haris', 'Bilal', 'Amin')
tuple2 = (1, 2, 3)
tuple3 = (5.5, 6.9, 99.99)
tuple4 = (5j, 9j)
tuple5 = (True, False)
tuple6 = (True, False, 'Haris', 'Bilal', 'Amin',
          5.5, 6.9, 99.99, 5j, 9j, 1, 2, 3)

# ============== Tuple Formatting =================

print('{}{}{}{}{}'.format(tuple1, tuple2, tuple3, tuple4, tuple5))
print('{}'.format(tuple1+tuple2+tuple3+tuple4+tuple5))

print('%s%s%s%s%s' % (tuple1, tuple2, tuple3, tuple4, tuple5))

print(f'{tuple1}{tuple2}{tuple3}{tuple4}{tuple5}')
print(f'{tuple1+tuple2+tuple3+tuple4+tuple5}')

# ================ Constructor ==================
myTuple = tuple(('Haris', 'Bilal', 'Amin'))
print(myTuple)

# =============== Difference =================
# Empty list, tuple, set
a = []
a = list()
b = ()
b = tuple()
c = {}  # its a dictionary not set
c = set()

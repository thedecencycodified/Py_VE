# ============== Comparisons Operators =================
# Equal to                  : ==
# Not Equals to             : !=
# Greater Than              : >
# Less Than                 : <
# Greater Than or Equals to : >=
# Less than or Equals to    : <=
# a = 5
# b = 6
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
#
# print(5 == 6)
# print(5 != 6)
# print(5 > 6)
# print(5 < 6)
# print(5 >= 6)
# print(5 <= 6)
#
# ============== Logical Operators =================
# AND
# ------------
# a . b = c
# ------------
# 0 . 0 = 0 f.f=f
# 1 . 0 = 0 t.f=f
# 0 . 1 = 0 f.t=f
# 1 . 1 = 1 t.t.t
# ------------
my_number = 5
print(my_number > 4 and my_number < 6)
print(my_number > 4 and my_number == 6)

# OR
# ------------
# a + b = c
# ------------
# 0 + 0 = 0 f+f=f
# 1 + 0 = 1 t+f=t
# 0 + 1 = 1 f+t=t
# 1 + 1 = 1 t+t=t
# ------------
my_number2 = 5
print(my_number2 > 4 or my_number2 < 6)
print(my_number2 > 4 or my_number2 == 6)
print(my_number2 < 4 or my_number2 == 6)
print(5 > 3 or 5 == 5)
print(5 < 3 or 5 == 5)
print(5 == 3 or 5 != 5)

# NOT
# a = b
# 1 = 0
# 0 = 1

my_number3 = 5
print(not my_number3)

# ============== Identity Operators =================
# is
# is not
a = 5
b = 5
print(a is b)
print(a is not b)

# ============== Membership Operators =================
# in
# not in
list = [1, 2, 3]
print(1 in list)
print(5 in list)
print(5 not in list)
print(3 not in list)

# ============== Bitwise Operators =================
# & AND
print(1 & 6)
print(1 & 1)

# | OR
print(1 | 6)
print(1 | 1)

# ^ XOR
print(1 ^ 6)
print(1 ^ 1)

# ~ NOT
print(~6)
print(~1)

# << Zero fill left shift

# >> right shift
#

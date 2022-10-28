# index     012345678910
greeting = 'Hello World'
print(greeting)
# ============index to item==============
print(greeting[0])
print(greeting[6])
print(greeting[10])
print(greeting[3])
# [(starting point):(limit)] # limit = 10 stops at 9th index
print(greeting[:])
print(greeting[2:])
print(greeting[:10])
print(greeting[0:11])
print(greeting[4:8])

# ============item to index==============
# index()
# index     012345678910
greeting = 'Hello World'
print(greeting.index('W'))
print(greeting.index('H'))
print(greeting.index('ell'))
print(greeting.index('ld'))

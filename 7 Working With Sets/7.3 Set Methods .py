"""
add()	        Adds an element to the set
clear()	        Removes all the elements from the set
copy()	        Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	    Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	    Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	        Removes an element from the set
remove()	    Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	        Return a set containing the union of sets
update()	    Update the set with the union of this set and others
"""
# ========== add() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.add(8)
print(set1)

# ========== clear() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.clear()
print(set1)

# ========== copy() ===============
set1 = {1, 2, 3}
set2 = set1.copy()
print(set2)

# ========== difference() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
diff = set1.difference(set2)
print(diff)
diff2 = set2.difference(set1)
print(diff2)

# ========== difference_update() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)

# ========== discard() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.discard(2)
print(set1)

# ========== intersection() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersect = set1.intersection(set2)
print(intersect)

# ========== intersection_update() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)

# ========== isdisjoint() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.isdisjoint(set2))

# ========== issubset() ===============
set1 = {1, 2, 3}
set2 = {3}

print(set2.issubset(set1))

# ========== issuperset() ===============
set1 = {1, 2, 3}
set2 = {3}

print(set1.issuperset(set2))

# ========== pop() ===============
set1 = {1, 2, 3}
set1.pop()
print(set1)

# ========== remove() ===============
set1 = {1, 2, 3}
set1.remove(3)
print(set1)

# ========== union() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# ========== update() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

# ========== symmetric_difference() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
syDiff = set1.symmetric_difference(set2)
print(syDiff)

# ========== symmetric_difference_update() ===============
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)

#Is a collection type that is unordered, mutable, and does not allow duplicate elements. 
# Sets are commonly used to store unique items and to perform mathematical set operations like union, intersection, and difference.

#Characteristics

# Unordered: The elements in a set do not have a specific order. DOENOT FOLLOW INDEXING & SLICING
# Mutable: You can add or remove elements from a set after it has been created.
# No Duplicates: Sets automatically remove duplicate elements, so each item in a set is unique.


#Syntax
#SETS are created using CURLY brackets {}, with elements separated by commas.

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Creating an empty set
empty_set = set()
print(empty_set)

#Adding Elements:
my_set.add(6)
print(my_set)

#Removing Elements:
my_set.remove(3)
print(my_set)

#Checking Membership:    DOEST IN MY SET 4 CONTAINS
print(4 in my_set)  # True

#Set Operations:
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)  # {1, 2, 3, 4, 5}
print(union_set)

# Intersection
intersection_set = set_a.intersection(set_b)  # {3}
print(intersection_set)

# Difference
difference_set = set_a.difference(set_b)  # {1, 2}
print(difference_set)
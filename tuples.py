#Is a collection type that is ordered and immutable. 
#This means that once a tuple is created, you cannot change its elements. Tuples are often used to group together related data.

#characteristics

#Ordered: The elements in a tuple have a specific order.
#Immutable: Once a tuple is created, you cannot change, add, or remove elements from it.
#Allows Duplicates: Tuples can contain duplicate elements.

#Syntax
#TUPLES are created using ROUND brackets (), with elements separated by commas.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Creating an empty tuple
empty_tuple = ()
print(empty_tuple)

# Creating a tuple with one element (note the comma)
one_element_tuple = (1,)
print(one_element_tuple)


# Accessing Elements
print(my_tuple[0])  # Accessing the first element (1)
print(my_tuple[-1])  # Accessing the last element (5)

#Unpacking Tuples:
a, b, c = (1, 2, 3)
print(a)  # 1
print(b)  # 2
print(c)  # 3

#Tuple Concatenation:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

#Checking Membership:
print(3 in my_tuple)  # True




#Tuples are particularly useful when you need to ensure that the data remains unchanged throughout the program, 
# such as coordinates or fixed configurations. If you have more questions or need examples, feel free to ask!


#list is an ordered collection of elements that can be of any data type, such as numbers, strings, or even other lists. 
#Lists are highly versatile and are one of the most commonly used data structures in Python.

#Characteristics

#Ordered: Elements in a list have a defined order, and this order is preserved.
#Mutable: You can modify the elements of a list (add, remove, or change elements).
#Indexed: Elements can be accessed by their index, which starts at 0.
#Heterogeneous: A list can contain elements of different data types.

#Syntax
#Lists are created using square brackets [], with elements separated by commas.

my_list = [1, 2, 3, 4, 5]
my_mixed_list = [1, "hello", 3.14, True, [5, 6, 7]]
print(my_list)
print(my_mixed_list)

#Accessing Elements
#You can access elements by their index:

first_element = my_list[0]  # Outputs 1
print(first_element)

last_element = my_list[-1]  # Outputs 5 (negative index    means slicing)
print(last_element)


#Modifying Lists
#Lists are mutable, so you can add, remove, or change elements:

# Adding elements
my_list.append(6)          # Adds 6 at the end
print(my_list)

my_list.insert(2, "new")   # Inserts "new" at index 2
print(my_list)

# Removing elements
my_list.remove("new")
print(my_list)      # Removes the first occurrence of "new"

popped_element = my_list.pop()  # Removes and returns the last element
print(popped_element)

# Changing elements
my_list[0] = 10            # Changes the first element to 10
print(my_list)

#Common List Operations
#Slicing: Extract a part of the list.

sub_list = my_list[1:4]  # Outputs [2, 3, 4]
print(sub_list)


#indexing and slicing

# ->                    0        1         2            # indexcing
names : list[str] = ["Qasim","Sir Zia", "Sir Inam"] 
# <-                    -3     -2          -1            # slicing

print(names[-2])
print(names[1])



# ->                    0        1         2
names : list[str] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-
print(names)
a : str = names.pop() # pop return method

print(a)
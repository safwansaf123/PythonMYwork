#In Python, the terms mutable and immutable refer to the ability (or inability) of an object to be changed after it has been created

#Mutable Objects
#that can be modified after they are created. This means you can change their contents, add or remove elements, etc.

# list
my_list = [1, 2, 3]
my_list.append(4)  # Now my_list is [1, 2, 3, 4]
print(my_list)

# Dictionaries:
my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 26  # Now my_dict is {"name": "Alice", "age": 26}
print(my_dict)

#set
my_set = {1, 2, 3}
my_set.add(4)  # Now my_set is {1, 2, 3, 4}
print(my_set)


#Immutable Objects
#cannot be changed after they are created. Any attempt to modify an immutable object will result in the creation of a new object.
# by concatenation method

#Strings:
my_string = "Hello"                 # can add in it
new_string = my_string + " World"  # Creates a new string "Hello World"
print(new_string)

#Tuples:
my_tuple = (1, 2, 3)          # can add in it
new_tuple = my_tuple + (4,)  # Creates a new tuple (1, 2, 3, 4)
print(new_tuple)

#Integers:
my_int = 10            # can add in it
new_int = my_int + 5  # Creates a new integer 15
print(new_int)
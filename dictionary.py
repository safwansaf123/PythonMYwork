#Is a collection type that is unordered, mutable, and indexed by keys. 
# Dictionaries allow you to store data in key-value pairs, which makes them very useful for organizing and accessing data quickly.

#characteristics

#Unordered: The elements in a dictionary do not have a specific order.
#Mutable: You can add, remove, or change key-value pairs after the dictionary has been created.
#Indexed by Keys: Each value in a dictionary is accessed using a unique key.

#Syntax
#SETS are created using CURLY brackets {}, with elements separated by commas.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

# Creating an empty dictionary
empty_dict = {}
print(empty_dict)

#Accessing Values:
print(my_dict["name"])  # Accessing the value associated with the key "name" (Alice)

#Adding or Updating Key-Value Pairs:
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
print(my_dict)
my_dict["age"] = 31  # Updating the value associated with the key "age"
print(my_dict)

#Removing Key-Value Pairs:
del my_dict["city"]  # Removing the key-value pair with the key "city"
print(my_dict)

#Checking Membership:
print("name" in my_dict)  # True
print("city" in my_dict)  # False (since it was removed)

#Iterating in a dictionary means going through each key-value pair in the dictionary to access or manipulate the elements
#Iterating Over Keys and Values:

# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

#Iterating Over Values Only:
for value in my_dict.values():
    print(value)

#Using enumerate to Get Index Along with Keys:
for index, key in enumerate(my_dict):
    print(index, key,)     

#This method allows you to access the index of each key along with the key and its corresponding value.



#Dictionaries are particularly useful when you need to associate pieces of data with unique identifiers, such as storing information 
#about students by their student IDs or configuration settings by their names.
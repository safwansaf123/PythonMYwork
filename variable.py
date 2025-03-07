#Variables in Python are used to store data values, and they are fundamental to programming

#1. Declaring Variables
#In Python, you declare a variable by simply assigning a value to it using the = operator:

x = 5
name = "Alice"
is_active = True       # first letter must be capital T
list_data = [1,2,3,4,5,6]    # square brackets    Array in typscript,  List in python 
tuple_data = (1,2,3,4,5,6)   # round brackets     Tuple in typscript,   Tuple in python    same
set_data = {1,2,3,4,5,6}     # curly brackets     
dic_data = { "safwan", "marium", "rimsha", "reeha", "anie", "salma" } # curly brackets
none_data = None

#2. Variable Types
#Python is dynamically typed, so you don't need to specify the type of a variable. 
#The type is determined at runtime based on the value assigned. Common data types include:

#int: Integer numbers, e.g., x = 5
#float: Floating-point numbers, e.g., y = 3.14
#str: Strings, e.g., name = "Alice"
#bool: Boolean values, e.g., is_active = True
#list: Lists, e.g., numbers = [1, 2, 3, 4]
#tuple: Tuples, e.g., coordinates = (10, 20)
#dict: Dictionaries, e.g., student = {"name": "Alice", "age": 21}
#set: Sets, e.g., unique_numbers = {1, 2, 3}    set is unordered  not like this [0],[1] also have unique values


# Global Variables: Declared outside of functions and accessible throughout the code.
# Local Variables: Declared inside functions and accessible only within those functions.

#Example Code
# Global variable:
PI = 3.14159

# Local variable:
def calculate_area(radius):
    # Local variable
    area = PI * (radius ** 2)
    return area

radius = 5
print("The area of the circle is:", calculate_area(radius))



print(x)
print(name)
print(is_active)
print(list_data)
print(tuple_data)
print(set_data)
print(dic_data)
print(none_data)
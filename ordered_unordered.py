#example of ordered or unordered in  list and set and tuples

names1 = ["safwan", "marium", "rimsha", "reeha", "anie", "salma"]  # list  is ordered 
names2 = {"safwan", "marium", "rimsha", "reeha", "anie", "salma"}  # set is  un ordered  sequence not followed
names3 = ("safwan", "marium", "rimsha", "reeha", "anie", "salma")  # tuples is oredered

print(names1) #['safwan', 'marium', 'rimsha', 'reeha', 'anie', 'salma']
print(names2) #{'salma', 'rimsha', 'reeha', 'safwan', 'marium', 'anie'}
print(names3) #['safwan', 'marium', 'rimsha', 'reeha', 'anie', 'salma']


#Key Points about Sets:

#Unordered: The elements have no specific order.
#Unique Elements: Sets do not allow duplicate elements.
#Mutable: You can add or remove elements from a set

names2 = {"safwan", "marium", "rimsha", "reeha", "anie", "salma","safwan", "marium", "rimsha"} # set unique  values means not repeat the values
print(names2) #{'salma', 'rimsha', 'reeha', 'safwan', 'marium', 'anie'}

names2 = {1,2,3,4,5,6,7,8,9}
print(names2) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

names2 = {1,2,3,4,5,7,8,9,1,2,3,4,5,6,7,8,9}  # in set unique values only no repeat values
print(names2) #{1, 2, 3, 4, 5, 6, 7, 8, 9}



#Key Points about tuples:
#This means the elements in a tuple have a defined order, and you can access elements by their position (or index). 
#Once a tuple is created, this order does not change.
names3 = ("safwan", "marium", "rimsha", "reeha", "anie", "salma")
print(names3[1])  # Output: marium

#Key Points about list:
#This means the elements in a list have a defined order, and you can access elements by their position (or index). 
#The order of elements is maintained throughout the list's lifetime.
names1 = ["safwan", "marium", "rimsha", "reeha", "anie", "salma"]
print(names1[3]) # Output: reeha
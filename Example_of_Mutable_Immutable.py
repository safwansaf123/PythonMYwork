#example of mutable and immutable  list and tuple and set

names1 = ["safwan", "marium", "rimsha", "reeha", "anie", "salma"]  # list    mutable
names3 = {"safwan", "marium", "rimsha", "reeha", "anie", "salma"}  # set     mutable 
names2 = ("safwan", "marium", "rimsha", "reeha", "anie", "salma")  # tuple   immutable   done by concatenations
print(names1)
print(names2)
print(names3)

#list
names1[0] = "aneeq"    # changes made in list   adding aneeq at 0
print(names1)          # ['aneeq', 'marium', 'rimsha', 'reeha', 'anie', 'salma']     changed

#tuple
#names2[0] = "ayesha"   # in tuple, cant change
#print(names2)          # here error      not changed

new_names = names2 + ("ayesha", )   # in tuple it will add in last     concatenation
print(new_names)  #('safwan', 'marium', 'rimsha', 'reeha', 'anie', 'salma', 'ayesha')

# Create a new tuple with changes to different locations
new_names = names2[:3] + ("saffoo",)  # in tuple it will add at location 3
print(new_names) #('safwan', 'marium', 'rimsha', 'saffoo')

new_names = names2[3:] + ("saffoo",)  # in tuple it will add after counting 3
print(new_names) #('reeha', 'anie', 'salma', 'saffoo')

#set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Add an element
my_set.remove(3)  # Remove an element
print(my_set)  #{1, 2, 4, 5, 6}                sequence of [0],[1],[2],[3],[4],[5] not followed
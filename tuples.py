# Tuple: ordered, inmutable, allows duplicate elements with different data types

# *** Creating and iterating over a tuple will be more efficiently compared to a list ***

# Creating tuples:
# first way using the '(,)' syntax
mytuple = ("Max", 29, "NY") # ('Max', 29, 'NY')

# second way using the tuple method built-in
mytuplev2 = tuple(["Marie", "Daniel", "Alex"]) # ('Marie', 'Daniel', 'Alex')

# accessing to a tuple element with indexes:
first_item = mytuplev2[0] # "Marie"

last_item = mytuplev2[-1] # "Alex"

# validating if an element exists into a tuple:
if "Sss" in mytuple: # no
    print("yes")
else:
    print("no")

# Get the lenght of a tuple:
letters_tuple = ("d", "a", "n", "i", "i")
len_letters = len(letters_tuple) # 5

# Counting the number of occurrences of an element into the tuple
number_of_occurrences = letters_tuple.count("i") # 2

# Get the index of the first occurrence from the tuple, and if the values does not exists into the tuple will raise a ValueError
index_number = letters_tuple.index("i") # 3

# Slicing tuples:
tuple_numbers = (1, 2, 3, 4, 5)

slice_tuple = tuple_numbers[:3] # (1, 2, 3)
odd_numbers = tuple_numbers[::2] # (1, 3, 5)
even_numbers = tuple_numbers[1::2] # (2, 4)

# reversing a tuple
reversed_tuple = tuple_numbers[::-1] # (5, 4, 3, 2, 1)

# unpacking tuples:
user_data = ("Marie", "Sujan", 23, "Texas")

# the number of elements to unpack must macth with the number of elements inside the tuple, if this previous condition does not satifies a value error will be raised
name, surname, age, location = user_data # Marie Sujan 23 Texas


# unpacking elements from a tuple with the "*" syntax:
large_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# the index1to7 element will be a list with the values corresponding to the value's tuple missed
index0, *index1to7, index8, index9, index10 = large_tuple # 0 [1, 2, 3, 4, 5, 6, 7] 8 9 10






















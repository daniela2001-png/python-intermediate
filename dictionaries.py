# Dictionary:is a collection of Key-value pairs, Unordered, Mutable

# ***The keys of a dictionary will be always inmmutable keys like: sets, tuples, ints, strings ... ***

# Creating dictionaries:

# first way: using the "{}" syntax
mydict = {
    "key": "value", "key2": "value2"
}

# second way: using the built-in method dict()
mydictv2 = dict(name="Max", age=23, location="Berlin") # {'name': 'Max', 'age': 23, 'location': 'Berlin'}

# Adding new keys into a dictionary:
mydictv2["email"] = "max@email.com" # {'name': 'Max', 'age': 23, 'location': 'Berlin', 'email': 'max@email.com'}

# Overwrtting key-values into a dictionary:
mydictv2["email"] = "updated_max@email.com" # {'name': 'Max', 'age': 23, 'location': 'Berlin', 'email': 'updated_max@email.com'}


# Accessing into a dictionary:

# first way: using the "[]" syntax, if the key does not exists a KeyError will be raised
mydictv2["name"] # "Max"


# second way: using the get() method, if the key does not exists and we do not sets a default value in case does not exists, we'll get a None value
mydictv2.get("working_hours", 0) # the output will be equal to 0, because the key working_hours does not exists !


# Deleting keys of a dictionary:

# first way: using the "del" method:
del mydictv2["email"] # {'name': 'Max', 'age': 23, 'location': 'Berlin'}

# second way: Using pop method if key is not found, default is returned if given, otherwise KeyError is raised
deleted_value = mydictv2.pop("age") # returns 23 and delete the age key from the dictionary.

# Removes the last inserted item from the dictionary
mydictv2.popitem() # {'name': 'Max'}

# Validating if a key exists into the dictionary:

# first way: using and if statement
if "name" in mydictv2:
    print("exists")
else:
    print("not exists")

# second way using try:except statement:
try:
    print(mydictv2["name"])
except KeyError as error:
    print(error)

# Iterating over a dictionary:
for key, value in mydictv2.items():
    print(f"{key} -> {value}")


# Copying dictionaries:

# first way: using pointers (modifies the original dictionary can be a dangerous behaviour !!!)
my_original_dictionary = dict(high=23.90, width=356.90, degree_angle=97.67)
my_copy_pointer_dict = my_original_dictionary # if we change my_copy_pointer_dict the my_original_dictionary will change as well

# second way:  Creating a copy without pointers (no alterate the original dictionary):
my_copy_without_pointers = dict(my_original_dictionary)


# Merging and Updating dictionaries:
sample_one = {"name": "Marie", "surname": "Liss", "location": "UK"}
sample_two = {"name": "Dani", "age": 23, "job": "software developer"}

# Here the common key will be overwritten with the last dictionary, in this case sample_two, and finally both will be merged it
sample_one.update(sample_two) # sample_one -> {'name': 'Dani', 'surname': 'Liss', 'location': 'UK', 'age': 23, 'job': 'software developer'}

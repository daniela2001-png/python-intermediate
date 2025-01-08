# Lists: ordered, mutable allows duplicate elements
mylist = ["banana", "cherry", "apple"]

# data types differents
mylist2 = [5, True, "apple"]


# validates if an element is into the list
if "banana" in mylist2:
    print("yes")
else:
    print("no")

# append elements at the end
mylist2.append("lemon") # [5, True, 'apple', 'lemon']

# insert elements at the index given
mylist2.insert(1, "one") # [5, 'one', True, 'apple', 'lemon']

# delete the last element of the list (IndexError: pop index out of range if the  index does not exists)
item_to_delete = mylist2.pop() # [5, 'one', True, 'apple']

# remove the first occurrence of the element by value: (Raises ValueError if the value is not present.)
mylist2.remove('apple') # [5, 'one', True]


# reverse a list
mylist2.reverse() # [True, 'one', 5]

# sort a list, sorted by default in ascending order
mylist.sort() # ['apple', 'banana', 'cherry']

# sort a list, sorted in descending order using the reverse parameter == True
mylist.sort(reverse=True) # ['cherry', 'banana', 'apple']

# if we don't want to modify the original list, we can use the sorted method:
my_new_updated_list = sorted(mylist)

# creating a list wiht the same value multiple times:
my_list_with_repeated_values = [2] * 6 # [2, 2, 2, 2, 2, 2]

# concatenating lists:
new_list = my_list_with_repeated_values + mylist # [2, 2, 2, 2, 2, 2, 'cherry', 'banana', 'apple']

# slicing lists ([start_index:stop_index])
new_ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_ordered_slice = new_ordered_list[2:7] # [3, 4, 5, 6, 7]


# advanced slicing ([start_index:stop_index:step])
my_ordered_slice_v2 = new_ordered_list[::2] # [1, 3, 5, 7, 9] goes 2 in 2 through all the list from zero index to the last index

# reversing the list using slicing:
my_reversed_slice = new_ordered_list[::-1] # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# copying lists:
my_original_list = ["dani", "andy", "danna", "marie"]

# first way:
my_copy_list = my_original_list # here we creates a pointer to my_original_list, so the cahnges that i made in the copy will be reflected into the original list

# second way:
my_copy_list_v2 = my_original_list.copy() # creates a new address in memory, so the original list will not modified

# third way:
my_copy_list_v3 = my_original_list[:] # creates a new address in memory, so the original list will not modified


# Comprehension lists: are a fast way to create new lists from an existent list in one line
# new_ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = [number*number for number in new_ordered_list] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# deletes all elements from the list
mylist2.clear() # []








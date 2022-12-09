# #!/usr/bin/python3
# Write a function that returns a list with all values multiplied by a number without using any loops.
#
# Prototype: def multiply_list_map(my_list=[], number=0):
# Returns a new list:
# Same length as my_list
# Each value should be multiplied by number
# Initial list should not be modified
# You are not allowed to import any module
# You have to use map
# Your file should be max 3 lines
# !/usr/bin/python3

def multiply_list_map(my_list, number=0):
    return list(map(lambda x: x * number, my_list))


my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
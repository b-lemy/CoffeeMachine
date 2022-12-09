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


# Write a function that computes the square value of all integers of a matrix using map
# Prototype: def square_matrix_map(matrix=[]):
# matrix is a 2 dimensional array
# Returns a new matrix:
# Same size as matrix
# Each value should be the square of the value of the input
# Initial matrix should not be modified
# You are not allowed to import any module
# You have to use map
# You are not allowed to use for or while
# Your file should be max 3 lines
# !/usr/bin/python3
def square_matrix_map(matrix):
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

# #!/usr/bin/python3
# Write a function that deletes keys with a specific value in a dictionary.
# Prototype: def complex_delete(a_dictionary, value):
# If the value does not exist, the dictionary won’t change
# All keys having the searched value have to be deleted
# You are not allowed to import any module

from MoreList2 import print_sorted_dictionary


def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return a_dictionary


a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

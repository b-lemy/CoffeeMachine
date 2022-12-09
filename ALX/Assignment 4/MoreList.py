sum = lambda x, y: x + y
print(sum(3, 4))


# Write a function that computes the square value of all integers of a matrix.
#
# Prototype: def square_matrix_simple(matrix=[]):
# matrix is a 2 dimensional array
# Returns a new matrix:
# Same size as matrix
# Each value should be the square of the value of the input
# Initial matrix should not be modified
# You are not allowed to import any module
# You are allowed to use regular loops, map, etc.
# !/usr/bin/python3

def square_matrix_simple(matrix):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        print(matrix[i])
        new_matrix[i] = list(map(lambda x: x, matrix[i]))
        print(new_matrix)

    return new_matrix


matrix = [
    [list('sat')],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(len(matrix))


# Write a function that replaces all occurrences of an element by another in a new list.
#
# Prototype: def search_replace(my_list, search, replace):
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element
# You are not allowed to import any module
# !/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list


my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)


# Write a function that adds all unique integers in a list (only once for each integer).
# Prototype: def uniq_add(my_list=[]):
# You are not allowed to import any module
# !/usr/bin/python3
def uniq_add(my_list):
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        print(i)
        num += i

    return (num)


my_list = [1, 2, 3, 1, 4, 2, 5, -1]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

print(set(('apple', 'banana', 'cherry', 'apple')))


# Write a function that returns a set of common elements in two sets.
# Prototype: def common_elements(set_1, set_2):
# You are not allowed to import any module
# !/usr/bin/python3
def common_elements(set_1, set_2):
    return  set_1 ^ set_2


set_1 = {"Python", "C", 'Ruby', "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

def common_elements(set_1, set_2):
    return set_1 & set_2


set_1 = {"Python", "C", 'Ruby', "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

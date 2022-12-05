# Write a function that prints a matrix of integers.
#
# Prototype: def print_matrix_integer(matrix=[[]]):
# Format: see example
# You are not allowed to import any module
# You can assume that the list only contains integers
# You are not allowed to cast integers into strings
# You have to use str.format() to print integers
# #!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(' '.join('{:d}'.format(j) for j in i))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()


# Write a function that adds 2 tuples.
#
# Prototype: def add_tuple(tuple_a=(), tuple_b=()):
# Returns a tuple with 2 integers:
# The first element should be the addition of the first element of each argument
# The second element should be the addition of the second element of each argument
# You are not allowed to import any module
# You can assume that the two tuples will only contain integers
# If a tuple is smaller than 2, use the value 0 for each missing integer
# If a tuple is bigger than 2, use only the first 2 integers


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
print(add_tuple(tuple_a, (1,)))
print(add_tuple(tuple_a, ()))


#
# Write a function that returns a tuple with the length of a string and its first character.
#
# Prototype: def multiple_returns(sentence):
# If the sentence is empty, the first character should be equal to None
# You are not allowed to import any module

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else "None"
    tup = length, first_char
    return tup


sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print(f"Length: {length} - First character: {first}")


#
# Write a function that finds the biggest integer of a list.
#
# Prototype: def max_integer(my_list=[]):
# If the list is empty, return None
# You can assume that the list only contains integers
# You are not allowed to import any module
# You are not allowed to use the builtin max()

def max_integer(my_list):
    if len(my_list) == 0:
        return "None"
    x = my_list[0]
    for i in my_list:
        if i > x:
            x = i
    return x


my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

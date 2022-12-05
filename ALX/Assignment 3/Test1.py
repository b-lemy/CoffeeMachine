import string

print(string.ascii_uppercase)

__import__("os").write(1, "#pythoniscool\n".encode("UTF-8"))


# 5/12/2022
# Write a function that retrieves an element from a list like in C.
#
# Prototype: def element_at(my_list, idx):
# If idx is negative, the function should return None
# If idx is out of range (> of number of element in my_list), the function should return None
# You are not allowed to import any module
# You are not allowed to use try/except
def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        "None"


print(element_at([1, 2, 3, 4, 5], 2))


#
# Write a function that replaces an element of a list at a specific position (like in C).
#
# Prototype: def replace_in_list(my_list, idx, element):
# If idx is negative, the function should not modify anything, and returns the original list
# If idx is out of range (> of number of element in my_list), the function should not modify anything, and
# returns the original list
# You are not allowed to import any module
# You are not allowed to use try/except

def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list


print(replace_in_list([1, 2, 3, 4, 5], 3, 'we'))


# Write a function that prints all integers of a list, in reverse order.
#
# Prototype: def print_reversed_list_integer(my_list=[]):
# Format: one integer per line. See example
# You are not allowed to import any module
# You can assume that the list only contains integers
# You are not allowed to cast integers into strings
# You have to use str.format() to print integers

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        # print('{:d}'.format(i))
        print(f'{i}')


print(print_reversed_list_integer([1, 2, 4, 5, 56]))


# !/usr/bin/python
# Write a function that removes all characters c and C from a string.
#
# Prototype: def no_c(my_string):
# The function should return the new string
# You are not allowed to import any module
# You are not allowed to use str.replace()
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i != 'c' and i is not 'C':
            new_str += i
    return new_str


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
# return my_string.translate({ord(c): None for c in "cC"})


stri = "thisy is string example....wow!!! this is really string";
print(stri.replace("is", ""))
print(stri.replace("is", "was", 1))

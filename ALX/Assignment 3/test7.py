# Write a function that finds all multiples of 2 in a list.
#
# Prototype: def divisible_by_2(my_list=[]):
# Return a new list with True or False, depending on whether the integer
# at the same position in the original list is a multiple of 2
# The new list should have the same size as the original list
# You are not allowed to import any module

def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            boolist[count] = True
        else:
            boolist[count] = False
    return boolist


my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1


#
# Write a function that deletes the item at a specific position in a list.
#
# Prototype: def delete_at(my_list=[], idx=0):
# If idx is negative or out of range, nothing change (returns the same list)
# You are not allowed to use pop()
# You are not allowed to import any module
# !/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del (my_list[idx])
    return (my_list)


my_list = [1, 2, 3, 4, 5]
idx = -3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

# Complete the source code in order to switch value of a and b
# You can find the source code here
# Your code should be inserted where the comment is (line 4)
# Your program should be exactly 5 lines long

#!/usr/bin/python3
a = 89
b = 10

a, b = b, a
# or
# c = a
# a = b
# b = c
print(a)
print("a={:d} - b={:d}".format(a, b))

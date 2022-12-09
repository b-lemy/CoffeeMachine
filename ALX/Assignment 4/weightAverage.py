#!/usr/bin/python3
# Write a function that returns the weighted average of all integers tuple (<score>, <weight>)
#
# Prototype: def weight_average(my_list=[]):
# Returns 0 if the list is empty
# You are not allowed to import any module

def weight_average(my_list):
    if not my_list:
        return 0

    num = 0
    den = 0

    for tup in my_list:
        print(tup)
        num += tup[0] * tup[1]
        print(num)
        den += tup[1]
        print(den)

    return num / den


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

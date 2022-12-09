# Write a function that returns the number of keys in a dictionary.
# Prototype: def number_keys(a_dictionary):
# You are not allowed to import any module

# !/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())
    print(list_keys)

    for i in list_keys:
        num += 1

    return num


a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
nb_keys = number_keys(a_dictionary)
print(f'Number of keys: {nb_keys}')

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    print(list_ord)
    list_ord.sort()
    for i in list_ord:
        print(i)
        print("{}: {}".format(i, a_dictionary.get(i)))


a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Write a function that replaces or adds key/value in a dictionary.

# Prototype: def update_dictionary(a_dictionary, key, value):
# key argument will be always a string
# value argument will be any type
# If a key exists in the dictionary, the value will be replaced
# If a key doesn’t exist in the dictionary, it will be created
# You are not allowed to import any module

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return (a_dictionary)


a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
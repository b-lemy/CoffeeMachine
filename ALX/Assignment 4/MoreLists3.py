# #!/usr/bin/python3
# Write a function that returns a new dictionary with all values multiplied by 2
#
# Prototype: def multiply_by_2(a_dictionary):
# You can assume that all values are only integers
# Returns a new dictionary
# You are not allowed to import any module
from MoreList2 import print_sorted_dictionary


def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())
    print(list_keys)

    for i in list_keys:
        print(new_dir[i])
        new_dir[i] *= 2

    return new_dir


a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)


# Write a function that returns a key with the biggest integer value.
# Prototype: def best_score(a_dictionary):
# You can assume that all values are only integers
# If no score found, return None
# You can assume all students have a different score
# You are not allowed to import any module
# !/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    return max(a_dictionary, key=a_dictionary.get)


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print(a_dictionary.get('Molly'))

print("Best score: {}".format(best_key))

best_key = best_score(None)
print(f"Best score: {best_key}")


print(max("Mike", "John", "Vicky"))

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

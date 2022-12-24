# Lists are mutable, and hence, they can be altered even after their creation.
# Dictionary in Python on the other hand is an unordered collection of data values,
# used to store data values like a map, which unlike other Data Types that hold only single value as
# an element, Dictionary holds key:value pair
# List Comprehension
numbers = [1, 2, 3, 4]
array = []
for n in numbers:
    n = n * 2
    array.append(n)

print(array)

# with list comprehension
# new_list = [new_list for item in list]
new_list = [n * 3 for n in numbers]
print(new_list)

name = 'Brian'
new_name = [letter for letter in name]
print(new_name)

# new_list = [new_list for item in list if test]
new_nam = [letter for letter in name if letter != 'n']
print(new_nam)


with open('file.txt') as file_1:
    file_data = file_1.readlines()

print(file_data)
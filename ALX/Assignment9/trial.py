a = 100
b = a
print(id(a))
print(id(b))

numbers = [17, 123]
print(numbers[9 - 8])

# horsemen = ["war", "famine", "pestilence", "death"]
# i = 0
# num = len(horsemen)
# while i < num:
#     print(horsemen[i])
#     i += 1

horsemen = ['war', 'famine', 'pestilence', 'death']
print('pestilence' in horsemen)

numbers = [1, 2, 3, 4, 5]
print(len(numbers) - 1)

for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2

print(numbers)

for index, value in enumerate(['banana', 'apple', 'pear', 'quince']):
    # numbers[index] = value ** 2
    print(index, value)

a = 100
b = a + 1
print(id(a))
print(id(b))

s1 = "Best School"
s3 = "Best School"
s2 = s1
print(s1 is s3)

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

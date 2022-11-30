i = 3


if i % 15 == 0:
    print("FizzBuzz", end='')
elif i % 3 == 0:
    print("Fizz", end='')
elif i % 5 == 0:
    print("Buzz", end='')
else:
    print(i, end='')

print(' \n', end='')


for ch in reversed(range(97, 123)):

    print("{:c}".format(ch if (ch % 3 == 0) else (ch - 32)), end='')



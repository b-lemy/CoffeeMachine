def islower(c):
    if 97 <= ord(c) <= 122:

        return True

    else:

        return False


#
# def uppercase(str):
#     for i in range(len(str)):
#
#         if 97 <= ord(str[i]) <= 122:
#
#             num = 32
#
#         else:
#
#             num = 0
#
#         print("{:c}".format(ord(str[i]) - num), end='')
#
#     print()
#

def print_last_digit(numb):
    if numb >= 0:
        l_digit = numb % 10
        print(l_digit)
    else:
        l_digit = numb % -10
        l_digit *= -1
        print(l_digit)

# print("{:d}".format(l_digit), end='')
# return l_digit


print_last_digit(104)

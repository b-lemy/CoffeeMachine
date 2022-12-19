def safe_print_list(my_list, x=0):
    ret = 0
    for i in range(x):
        print(i)

        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
            print('-')
            print(ret)
        except IndexError:
            print('see')
    print("")
    return ret


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 6)
print("nb_print: {:d}".format(nb_print))


# nb_print = safe_print_list(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))


# Write a function that divides 2 integers and prints the result.
#
# Prototype: def safe_print_division(a, b):
# You can assume that a and b are integers
# The result of the division should print on the finally: section preceded by Inside result:
# Returns the value of the division, otherwise: None
# You have to use try: / except: / finally:
# You have to use "{}".format() to print the result
# You are not allowed to import any module


def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end=" ")
            ret += 1
        except (ValueError, TypeError):
            print('err')
    print("")
    return ret


# my_list = [1, 2, 3, 4, 5]
#
# nb_print = safe_print_list_integers(my_list, 2)
# print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))


# nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))


# Write a function that divides 2 integers and prints the result.
#
# Prototype: def safe_print_division(a, b):
# You can assume that a and b are integers
# The result of the division should print on the finally: section preceded by Inside result:
# Returns the value of the division, otherwise: None
# You have to use try: / except: / finally:
# You have to use "{}".format() to print the result
# You are not allowed to import any module

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

# Write a function that divides element by element 2 lists.
#
# Prototype: def list_division(my_list_1, my_list_2, list_length):
# my_list_1 and my_list_2 can contain any type (integer, string, etc.)
# list_length can be bigger than the length of both lists
# Returns a new list (length = list_length) with all divisions
# If 2 elements can’t be divided, the division result should be equal to 0
# If an element is not an integer or float:
# print: wrong type
# If the division can’t be done (/0):
# print: division by 0
# If my_list_1 or my_list_2 is too short
# print: out of range
# You have to use try: / except: / finally:
# You are not allowed to import any module
def list_division(my_list_1, my_list_2, list_length):
    # print(max(len(my_list_1), len(my_list_2)))
    # print(my_list_2)

    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]

            print(div)
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list


my_l_1 = [10, 8, 4]
my_l_2 = [2, 0, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)


# print("--")
#
# my_l_1 = [10, 8, 4, 4]
# my_l_2 = [2, 0, "H", 2, 7]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

#
# Write a function that raises a type exception.
#
# Prototype: def raise_exception():
# You are not allowed to import any module

def raise_exception():
    """Raise a TypeError exception."""
    raise TypeError


try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

#
# Write a function that prints an integer.
#
# Prototype: def safe_print_integer_err(value):
# value can be any type (integer, string, etc.)
# The integer should be printed followed by a new line
# Returns True if value has been correctly printed (it means the value is an integer)
# Otherwise, returns False and prints in stderr the error precede by Exception:
# You have to use try: / except:
# You have to use "{:d}".format() to print as integer
# You are not allowed to use type()

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False


value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

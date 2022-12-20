# Write an empty class Square that defines a square:
class Square:
    def __init__(self, size):
        self.size = size


class Rectangle:
    pass


# The pass means incase the class is empty no errors will occur it will just pass


class Squarely:
    """Represent a square."""

    def __init__(self, size=5):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size


my_square_1 = Squarely()
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except:
    print('E')

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Squarely(5)
print("Area: {}".format(my_square_2.area()))

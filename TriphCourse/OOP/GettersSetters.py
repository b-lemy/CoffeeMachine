
class Squarely:
    """Represent a square."""

    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        print(self.__size)
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print(value)
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size


my_square = Squarely(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)



class Square:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

        print(height)

    @property
    def height(self):
        print('Retrieving Height')

        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print('please enter a digit')

    @property
    def width(self):
        print('Retrieving width')

        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print('please enter a digit')

    def getArea(self):
        return int(self.__height) * int(self.__width)


def main():
    area = Square()

    height = input('enter Height')
    width = input('enter width')

    area.height = height

    area.width = width

    print('the area is ', area.getArea())

main()

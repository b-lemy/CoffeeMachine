print(sum(i for i in range(10)))  # sum of squares

xvec = [1, 2, 2]
yvec = [2, 2, 2]
print(sum(x * y for x, y in zip(xvec, yvec)))  # dot product

data = 'golf'
print(len(data))
print(list(data[i] for i in range(len(data) - 1, -1, -1)))


class Base:
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances


for i in range(3):
    b = Base()
print(b.id)


class Base:
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances


class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()


u = User()
print(u.id)


class Vehicles:

    # Constructor
    def __init__( vehicleType ):
        print('Vehicles is a ', vehicleType)


# Defining Child class
class Car(Vehicles):

    # Constructor
    def __init__(self):
        Vehicles.__init__('Car')


# Driver's code
print(issubclass(Car, Vehicles))
print(issubclass(Car, list))
print(issubclass(Vehicles, Car))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicles)))

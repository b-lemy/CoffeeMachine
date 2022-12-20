def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):


        try:
            if i > a:
                print(a)
                raise Exception('Too far')

            else:
                print(i)
                result += a ** b / i
                print(result)
        except (TypeError, NameError, ValueError, IndexError):
            print('hello')
            result = b + a
            print(result)
        break
        return 'hello'


a = 1
b = 2
print( magic_calculation(a, b))

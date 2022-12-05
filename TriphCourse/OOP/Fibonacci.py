def fib2(n):  # return Fibonacci series up to n

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        # They give me different output do you know what's the reason
        # this
        a, b = b, a + b

        # or this

        a = b
        b = a + b

    return result


print(fib2(14))

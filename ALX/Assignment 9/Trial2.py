def increment(n):
    n += 1
    print(n)


a = 1
increment(a)
print(a)


def assign_value(n, v):
    n = v


l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)


def increment(n):
    n.append(4)
    print(n)


l = [1, 2, 3]
increment(l)
print(l)


a = (1, 2)
b = (1, 2)
print(a is b)

a = [1, 2, 3, 4]
print(id(a))
a = a + [5]
print(id(a))

a = [1, 2, 3]
print(id (a))
139926795932424
a += [4]
print(id(a))
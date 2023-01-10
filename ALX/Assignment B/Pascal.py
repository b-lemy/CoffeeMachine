def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n - 1):
        triangle.append([a + b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


print_triangle(pascal_triangle(3))


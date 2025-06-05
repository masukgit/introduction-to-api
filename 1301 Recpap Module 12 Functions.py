# # FIND MAXIMUM NUMBER FROM 3 NUMBERS
# def max_value(a, b, c):
#     """
#     This function will return the highest value
#     :param a, b, c: Any number
#     :return: Highest value
#     """
#     if c < a > b:
#     # if a > b and a > c:
#         return a
#     # elif b > a and b > c:
#     elif c < b > a:
#         return b
#     else:
#         return c
# print(max_value(39, 58, 12))
# print(float.__doc__)
#

def circle(radius):
    area = 2 * 3.1416 * radius * radius
    circum = 2 * 3.1416 * radius
    return area, circum
x = circle(5)
print(x)
print(type(x))

def sum(*args):
    """
    This will return sum of all numbers
    :param args: Any numbers separated by comma
    :return: Sum of all numbers
    """
    total = 0
    for arg in args:
        total += arg
    return total
print(sum(2, 5, 8, 1, 3))

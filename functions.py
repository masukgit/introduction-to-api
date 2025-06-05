def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def subs(first, second):
    result = first - second
    return result

def multiply(*numbers):
    multiplying = 1
    for number in numbers:
        multiplying *= number
    return multiplying

def division(first_num, second_num):
    divi_result = first_num / second_num
    return round(divi_result, 2)





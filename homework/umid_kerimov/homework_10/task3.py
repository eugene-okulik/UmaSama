def smart_operation(calc_func):
    def wrapper(num1, num2):
        if num1 == num2:
            return calc_func(num1, num2, '+')
        elif num1 < 0 or num2 < 0:
            return calc_func(num1, num2, '*')
        elif num1 > num2:
            return calc_func(num1, num2, '-')
        elif num2 > num1:
            return calc_func(num1, num2, '/')

    return wrapper


@smart_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second

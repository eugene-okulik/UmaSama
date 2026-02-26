def finish_me(func):
    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result

    return wrapper


@finish_me
def print_text(text):
    print(text)


print_text('print me')


@finish_me
def calc(x, y):
    print(x * y)


calc(6, 9)

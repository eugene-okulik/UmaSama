def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        result = None
        for _ in range(count):
            result = func(*args, **kwargs)
        return result

    return wrapper


@repeat_me
def print_text(text):
    print(text)


print_text('print_me', count=2)

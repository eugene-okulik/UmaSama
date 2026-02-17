import sys

sys.set_int_max_str_digits(1000000)


def fib_gen(index=10000000):
    num1 = 1
    num2 = 1
    pos = 0
    while pos < index:
        if pos == 0:
            yield 1
        else:
            num1, num2 = num2, num1 + num2
            yield num1
        pos += 1


count = 1
for i in fib_gen():
    if count in [5, 200, 1000]:
        print(i)
    elif count == 100000:
        print(i)
        break
    count += 1

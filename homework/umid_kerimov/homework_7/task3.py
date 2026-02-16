result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
result4 = 'результат: 2'


def result_sum(result):
    colon_index = result.index(':')
    number = int(result.index(':')[colon_index + 1:]) + 10
    print(number)

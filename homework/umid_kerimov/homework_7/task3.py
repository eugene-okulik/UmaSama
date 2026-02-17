result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
result4 = 'результат: 2'

answer = [result1, result2, result3, result4]


def result_sum(word):
    for i in word:
        result = int(i.split()[-1]) + 10
        print(result)


result_sum(answer)

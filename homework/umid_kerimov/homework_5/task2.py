result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

colon_index = result1.index(':')
number = int(result1[colon_index + 1:]) + 10
print(number)

colon_index = result2.index(':')
number = int(result2[colon_index + 1:]) + 10
print(number)

colon_index = result3.index(':')
number = int(result3[colon_index + 1:]) + 10
print(number)

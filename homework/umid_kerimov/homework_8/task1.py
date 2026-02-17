import random

salary = int(input('Indicate your salary: '))
bonus = random.choice([True, False])
bonus1 = random.randint(1, 10000)

if bonus is True:
    salary1 = salary + bonus1
    print(f"{salary}, {bonus} - '${salary1}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")

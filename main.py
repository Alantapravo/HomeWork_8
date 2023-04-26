N = int(input("Введіть будь-яке число, всі виведені числа будуть ділитися на 3: "))

i = 0
while i <= N:
    if not i % 3 != 0:
        print(i)
    i += 1

N = int(input("Введіть будь-яке число, буде виведена сума чисел які поділяються на 3 без залишку: "))

i = 0
summ = 0
while i <= N:
    if i % 3 == 0:
        summ += i
    i += 1

print(f'Sum even numbers from 1 to {N}: {summ}')

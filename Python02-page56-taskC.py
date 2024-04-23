n = input('Введите натуральное число:')
k = 0

for i in range(0,len(n)):
    k += int(str(n)[i])

print(f'Сумма цифр {k}')
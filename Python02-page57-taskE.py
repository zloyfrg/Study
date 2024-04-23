n = input('Введите натуральное число:')
res = set(list(n))
if len(n) == len(res):
    print('Нет')
else:
    print('Да')

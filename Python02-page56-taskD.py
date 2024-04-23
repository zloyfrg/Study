
n = input('Введите натуральное число:')
count = 0
for i in range(len(n)-1):
    if int(n[i])*int(n[i+1]) == int(n[i])**2:
        count += 1
        break
if not count:
            print('Нет')
else: print('Да')



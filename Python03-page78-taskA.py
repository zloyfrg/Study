"""
Заполнить массив случайными числами в интервале [-10,10]
и отобрать в другой массив все чётные отрицательные числа
"""

import random
# Генерируем случайную длину массива length_list длиной в диапазоне от 2 до 10
rand_list = []
a = []
b = []
length_list = random.randint(2, 10)

# Заполняем массив rand_list случайными числами в диапазоне от -10 до 10
while length_list:
    rand_list.append(random.randint(-10, 10))
    length_list -= 1
# Выводим получившийся массив
print(f'Массив:\n{rand_list}')

# Отбираем отрицательные чётные элементы в новый массив и выводим результат
for x in rand_list:
  if (x % 2 == 0) and (x < 0):
    b.append(x)
print(b)
"""
Заполнить массив случайными числами в интервале [0,100]
и отобрать в другой массив все простые числа.
Используйте логическую функцию, которая определяет,
является ли переданное ей число простым
"""
import random
# Генерируем случайную длину массива length_list длиной в диапазоне от 6 до 10
rand_list = []
length_list = random.randint(6, 10)

# Заполняем массив rand_list случайными числами в диапазоне от 0 до 100
while length_list:
    rand_list.append(random.randint(0, 100))
    length_list -= 1

# Выводим получившийся массив
print(f'Массив А:\n{rand_list}')

# Проверяем на простоту и вносим в результирующий список result_list
result_list = []
for x in rand_list:
    d = 2
    while d**2 <= x and x % d != 0:
        d += 1
        if d**2 > x:
            result_list.append(x)
print(f'Массив B:\n{result_list}')
"""
Заполнить массив случайными числами и выполнить циклический сдвиг элементов массива вправо на 1 элемент
"""
import random

# Генерируем случайную чётную длину массива length_list в диапазоне от 2 до 10
rand_list = []
length_list = random.randint(2, 10)

# Заполняем массив rand_list случайными числами в диапазоне от 1 до 50
while length_list:
    rand_list.append(random.randint(1, 50))
    length_list -= 1

# Выводим получившийся массив
print(f'Случайный массив: \n{rand_list}')

# Выполняем циклический сдвиг элементов массива вправо на 1 элемент
print(f'Циклический сдвиг элементов массива:\n{rand_list[len(rand_list)-1:]+rand_list[:len(rand_list)-1]}')




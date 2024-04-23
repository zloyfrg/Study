"""
Массив имеет четное число элементов.
Заполнить массив случайными числами
и выполнить реверс отдельно в первой половине и второй половине
"""
import random
# Генерируем случайную чётную длину массива length_list
rand_list = []
a = []
b = []
length_list = random.randint(1, 5)*2

# Заполняем массив rand_list случайными числами в диапазоне от 1 до 50
while length_list:
    rand_list.append(random.randint(1, 50))
    length_list -= 1
# Выводим получившийся массив
print(f'Массив:\n{rand_list}')
# Разворачиваем половинки и выводим результирующий массив
a = rand_list[:int(len(rand_list)/2)]
b = rand_list[int(len(rand_list)/2):]
a.reverse()
b.reverse()
print(f'Массив после реверса половинок:\n{a+b}')


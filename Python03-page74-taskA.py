"""
Заполнить массив случайными числами и выполнить циклический сдвиг элементов массива вправо на 1 элемент
"""
import random
rand_list = []
a = []
length_list = random.randint(2, 10)
while length_list:
    rand_list.append(random.randint(2, 50))
    length_list -= 1
print(f'Случайный массив: \n{rand_list}')
print(f'Циклический сдвиг элементов массива:\n{rand_list[len(rand_list)-1:]+rand_list[:len(rand_list)-1]}')




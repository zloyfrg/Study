"""
Заполнить массив случайными числами и отобрать в другой массив все числа Фибоначчи.
Используйте логическую функцию, которая определяет,
является ли переданное ей число числом Фибоначчи
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

# Заполним список fib_list числами Фибоначчи
f1 = f2 = 1
i = 0
n=9
fib_list = [1]
while i < n:
    f1, f2 = f2, f1 + f2
    fib_list.append(f2)
    i += 1
print(fib_list)



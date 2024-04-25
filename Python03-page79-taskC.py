"""
Заполнить массив случайными числами и отобрать в другой массив все числа Фибоначчи.
Используйте логическую функцию, которая определяет,
является ли переданное ей число числом Фибоначчи
"""
import random
# Генерируем случайную длину массива length_list длиной в диапазоне от 15 до 20
length_list = random.randint(15, 20)

# Заполняем массив rand_list случайными числами в диапазоне от 0 до 100
rand_list = []
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

# Выбираем числа Фибоначчи из сгенерированного списка и вносим в итоговый список result_list
result_list = []
for num in rand_list:
    for fib in fib_list:
        if num == fib:
            result_list.append(num)

print(f'Массив В:\n{sorted(result_list)}')



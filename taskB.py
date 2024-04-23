# Задача В
from math import sqrt

print('Вычисление длины отрезка по координатам двух точек')

ax = float(input('Введите координату Х точки А:'))
ay = float(input('Введите координату Y точки А:'))
bx = float(input('Введите координату Х точки B:'))
by = float(input('Введите координату Y точки B:'))

print(f'Длина отрезка AB = {sqrt(abs(ax-ay)**2+abs(bx-by)**2)}')


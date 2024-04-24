# Задача С
import random

number = random.randint(100, 999)
print(f'Получено число {number}', f'Его цифры {str(number)[0]}, {str(number)[1]}, {str(number)[2]}', sep='\n')
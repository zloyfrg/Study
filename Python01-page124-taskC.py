print('Введите последовательно:')
n1 = input('возраст Антона:')
n2 = input('возраст Бориса:')
n3 = input('возраст Виктора:')
b = {int(n1):'Антон',int(n2):'Борис',int(n3):'Виктор'}
a = [int(n1),int(n2),int(n3)]
a.sort()

print(f'{b[max(a)]} старше всех.')


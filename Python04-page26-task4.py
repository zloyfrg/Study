"""
Запишите регулярное выражение, соответствующее
вещественному числу (со знаком и без, с дробной частью и без, с целой частью и без)

"""
import re

s = '2.5^5!@-46 +1.623422=0.000566!f(-0asd+5asd123asdl;fk'
res = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)',s)
print(res)
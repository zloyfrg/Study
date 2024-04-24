import re

print(re.findall(r'[а-я].\d{2}[а-я]{2}\d{3}', '2.5^5!@-46 +1.6А234АА17422=0.000566!f(-0asd+5asd123asdl;fk', flags=re.IGNORECASE))
#Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.

import random

k = int(input())
result = ""
for i in range(k,-1,-1):
    koeff = random.randint(0,3)
    if koeff == 0:
        continue
    if koeff == 1:
        if i == 1:
            result += f"x+"
        elif i == 0:
            result += f"{koeff}"
        else:
            result += f"x**{i}+"
    else:
        if i == 1:
            result += f"{koeff}*x+"
        elif i == 0:
            result += f"{koeff}"
        else:
            result += f"{koeff}*x**{i}+"
result += " = 0"
print(result)

f = open("filepol.txt","w")
f.write(result)
f.close()
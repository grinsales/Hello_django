#Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в числах.
# Количество введенных чисел и искомая цифра задаются с клавиатуры.
# Числа выбираются рандомно.

import random
b = str(random.randint(1,100000000000000000000000000000000000000000000000000000000000000))
a = input("Введите,пожалуйста,цифру поиска от 0 до 9: ")
i=0
c=0
print(b)
for i in b:
    if i in a:
        c +=1
print(c)


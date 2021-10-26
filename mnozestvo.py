#Проверить, есть ли в последовательности чисел списка дубликаты.
import random
i=0
b=0
c=0
d=set()
b=[random.randint(0,10) for i in range(int(input("выберете количество элементов последовательности: ")))]
print(b)
for c in b:
 d.add(c)
print(d)
z=len(b)
h=len(d)
if z == h:
 print("в последовательности отсутствуют дубликаты")
 else:
 print("в последовательности есть дубликаты")



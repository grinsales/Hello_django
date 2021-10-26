#Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
q=[]
import random
i = 0
def recurs(s):
    while s != -1:
        return q[s]+q[recurs(s-1)]

while True:
    if i < 10:
        c = int(random.randint(1, 100))
        q.append(c)
        i=i+1
    else:
        break
print(q)
s=len(q)-1
print(recurs(s))

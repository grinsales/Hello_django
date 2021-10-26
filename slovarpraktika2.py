#Задача№2
#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
z = {}
w =[]
q=0
e=0
t=1

while True:
    a = input("Введите ключ для словаря или напишите слово конец: ")
    if a == "конец":
        break

    b = int(input("Введите значение ключа: "))

    z[a]=b
print(z)
a=z.values()
for q in a:
    w.append(q)
print(w)
for e in w:
    t *= e
print(t)

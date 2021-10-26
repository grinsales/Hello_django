#№3
#В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
#Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.
i=0
q=0
c=0
v=0
b=0
l=0
z = []
x = []

a=open("22.txt","r")
b=a.readlines()
print(b)
for i in b:
    z.append(i)
for q in range(len(z)):
    for v in z[q]:
        for b in v:
            if b.isdigit():
                x.append(int(b))
for l in x:
    if l<3:
        print(z[x.index((l))])
n=sum(x)//len(x)
print(f"средняя оценка учеников {n}")
a.close()
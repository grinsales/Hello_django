#Создайте функцию, которая принимает на вход неограниченное количество
# позиционных и именованных аргументов,
# в качестве результата функция должна возвращать только позиционные аргументы с нечетными
# индексами и ключевые, значения которых являются строками
i=0
c=0
e=0
d=[]
def func_1(*args,**kwargs):
    for i in range(len(args)):
        if i % 2 !=0:
            print(args[i])
    b=kwargs.items()
    for c in b:
       d.append(c)
    for e in range(len(d)):
        if type(d[e][1])==str:
            print(d[e][1])
func_1(1,2,3,4,5,a='asd',b=2,c=3,d=4,f="sdad")



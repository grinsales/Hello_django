#Задание 2
#Если в функцию передаётся кортеж, то посчитать длину всех его слов.
#Если список, то посчитать кол-во букв и чисел в нём.
#Число – кол-во нечётных цифр.
#Строка – количество букв.
#Сделать проверку со всеми этими случаями.


a =45


def fun1(*args):#функция кортежа
    print(f'длинна кортежа {len(a)}')
def fun2(*args): #функция списка
    i=0
    o=0
    p=0
    u=0
    for i in a:
        if isinstance(i, int):
            o +=1
        elif isinstance(i, str):
            p +=1
    print(f'количество цифр в списке: {o}')
    print(f'количество букв в списке: {p}')
def fun3(a): #функция числа
    i=0
    p=0
    for i in range(a+1):
        if i % 2!=0 and i!=0:
            p +=1
    print(f'количество нечетных чисел равно: {p}')
def fun4(a): #функция строки
    i=0
    p=0
    for i in a:
        p +=1
    print(f'количество букв в строке: {p}')



if isinstance(a, list):
    fun2(a)
elif isinstance(a, tuple):
    fun1(a)
elif isinstance(a, int):
    fun3(a)
elif isinstance(a, str):
    fun4(a)


    #i=0
    #o=0
    #p=0
    #u=0
    #for i in a:
        #if isinstance(i, int):
            #o +=1
        #elif isinstance(i, str):
            #p +=1
    #print(o)













#Пользователь вводит трехзначное число.
# Программа должна сложить цифры, из которых состоит это число.
# Например,
# если было введено 349, программа должна вывести на экран число 16, так как 3 + 4 + 9 = 16
summa=0
a=str(input("Введите трехзначное число: "))
for i in a:
    summa += int(i)
print(summa)





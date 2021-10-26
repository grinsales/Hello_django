#Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность


a = open('input.txt','w')
a.write("25 21")
a.close()
a = open('input.txt','r')
b=a.readline()
f = b.split()
print(f)
z=int(f[0])-int(f[1])
print(z)
f = open('output.txt','w')
f.write(str(z))
f.close()



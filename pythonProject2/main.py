#В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.
#a = open("1.txt","w")
#a.close()
i=0
n=0
a = open("1.txt","r")
b=a.readlines()
print(b)
c=len(b)
print("количество строк в ТХТ файле: ",c)
for i in b:
    n=n+1
    print(f"Количество символов в {n} строке равна: ", len(i))
a.close()






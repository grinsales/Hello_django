#Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длинны.
i=0
z = []
x = []
q = open("text2.txt","w")
a =q.readlines()
print(a)
for i in a:
    i=i[-1]
    print(i)
    if i.isalpha():
        print(i)

        z.append(i)
print(z)


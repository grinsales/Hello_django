import copy
class stroka:
    def __init__(self):
        self.vvod()
    def vvod(self):
        self.a=input("Введите число или строку: ")
        return self.a
    def fun1(self):
        return len(self.a)

ar=stroka()
x=ar.fun1()
w=copy.copy(x)
f=ar.a
h=copy.copy(f)

class stroka2:
    def __init__(self):
        self.vvod()
    def vvod(self):
        self.a = h
        return self.a
    def fun2(self):
        self.b=w
        return self.b
    def fun3(self):
        i = 0
        d = 0
        for i in self.a:  # вычленяем четные цифры числа
            if int(i) % 2 == 0:
                d += int(i)
         # uznaem dlinu 4isla
        return d * w
    def fun4(self):
        u = 0
        v = 0
        k = []
        j = []
        p = ["e", "y", "u", "i", "o", "a", "q"]
        o = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю", "ё"]
        for u in self.a:  # naidem 4islo glasnih
            if u in p or u in o:
                v += 1
                k.append(u)
            else:
                j.append(u)
        m = (w - v) * v
        if m <= w:
            return k
        else:
            return j

zx = stroka2()
if h.isdigit():
    print("произведение суммы чётных цифр на длину числа в числе: ", zx.fun3())
else:
    print(" если произведение гласных и согласных букв меньше или равно длине слова,выводить все гласные, иначе согласные: ",
            zx.fun4())


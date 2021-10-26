class calc:
    def __init__(self):
        self.vvod()
    def vvod(self):
        self.a=int(input("vvedite 1 4iclo: "))
        self.b=int(input("vvedite 2 4iclo: "))
    def plus(self):
        return self.a+self.b
    def minus(self):
        return self.a-self.b
    def umn(self):
        return self.a*self.b
    def dele(self):
        if b == 0:
            print("error")
        else:
            return self.a/self.b


while True:
    ex = calc()
    c = input("vvedite +,-,*,/,00: ")
    if c =="+":
        print(ex.plus())
    elif c =="-":
        print(ex.minus())
    elif c =="*":
        print(ex.umn())
    elif c =="/":
        print(ex.dele())
    elif c =="00":
        break











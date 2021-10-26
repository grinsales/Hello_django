class car():
    def __init__(self):
        self.ves="ves"
        self.cvet="cvet"
    def moddel(self):
        print(self.cvet)
        print(self.ves)

class moto(car):
    def __init__(self):
        super().__init__()
        self.kolesa = "kolesa:"
    def moddel(self):
        print(self.cvet)
        print(self.ves)
        print(self.kolesa)

def tip():
    for a in [car,moto]:
        print("++++")
        b=a()
        b.moddel()
tip()


class sum():
    def sum1(self,a,b,c,d=None):
        if d is None:
            print(a+b)
        else:
            print(a + b+c-d)
asfr=sum()
asfr.sum1(1,2,3)
asfr.sum1(1,2,3,4)
h

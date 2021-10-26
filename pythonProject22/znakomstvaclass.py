class skolko():
    def dengi(self):
        print("100rur")
a=skolko()
a.dengi()

class rur():
    @staticmethod
    def w100():
        print("100rur")
rur.w100()
ar=rur()
ac=rur()
ar.w100()
ac.w100()

class knigi():
    knigi = 0
    def __init__(self):
        knigi.knigi=knigi.knigi+100
    @classmethod
    def skolkoest(cls):
        print("na polke", cls.knigi)
class muzika(knigi):
    knigi=0
    def __init__(self):
        muzika.knigi=muzika.knigi+1
q=knigi()
w=knigi()
e=knigi()
r=knigi()
t=muzika()
t2=muzika()
t3=muzika()
knigi.skolkoest()
muzika.skolkoest()


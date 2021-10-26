violatorsongsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
q=0
w=0
e=0
r=0
t=0
z=[]
x=[]
c =[]
f=[]
g=[]
h={}
a=violatorsongsdict
b= a.values()
for q in b:
    z.append(q)
for w in z: # перевод все в секунды и подсчет общей продолжительности игры
    t=(w-w//1)*100+(w//1)*60 # перевод все в секунды
    w=w+1
    x.append(t)
u=sum(x)//60+(sum(x)-((sum(x)//60)*60))/100 # перевод суммы секунд обратно в начальную форму(мин.сек)
print("Общая продолжительноость игры альбома: ",u)
#Создайте список песен, время звучаниях которых больше 5 минут
#Создайте новый словарь тех песен, в название которых состоит из одного слова
s=a.items()
for e in s:
    c.append(e)
for r in range(len(c)):
    if c[r][1]>5:
        print('песня длинной больше 5 мин: ',c[r])
        f.append(c[r])
    if len((c[r][0]).split())==1:# считаем количество песен с одним словом
        g.append(c[r])
for t in range(len(g)):
    h[g[t][0]]=g[t][1]
print("новый альбом:",h)



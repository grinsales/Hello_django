import os

os.chdir("..")
os.chdir("..")
#os.mkdir("dz")

os.chdir("dz")
print(os.getcwd())
print("Все папки и файлы:", os.listdir())
a = open("test_1.txt", "w")
a.close()
os.chdir("..")
os.chdir("..")
#os.mkdir("dz")

os.chdir("dz")
print(os.getcwd())
print("Все папки и файлы:", os.listdir())

s = open("test_2.txt", "w")
s.close()
os.chdir("..")
os.chdir("..")
#os.mkdir("dz")

os.chdir("dz")
print(os.getcwd())
print("Все папки и файлы:", os.listdir())

d = open("test_3.txt", "w")
d.close()
print("Все папки и файлы:", os.listdir())









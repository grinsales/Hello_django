import sqlite3

a = [1, 24, 'dd', 'wedd', 'w', 23]
i = 0
conn = sqlite3.connect('1aq.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS BAZ1(id INTEGER PRIMARY KEY AUTOINCREMENT, col1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS BAZ2(id INTEGER PRIMARY KEY AUTOINCREMENT, col1 INTEGER)''')

for i in a:
    if type(i) is str:# выискиваем слова в списке
        cursor.execute('''INSERT INTO BAZ1(col1) VALUES(?)''',(i,)) # ДОбавляем в таблицу слова в
        conn.commit()
        cursor.execute('''INSERT INTO BAZ2(col1) VALUES(?)''', (len(i),)) # добавляем в таблицу цифр
        conn.commit()
    else:
        if i%2==0: #проверка цифр на четность
            cursor.execute('''INSERT INTO BAZ2(col1) VALUES(?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO BAZ1(col1) VALUES('НЕЧЕТНОЕ')''') #нечетные слова отправляем со словом нечетное в таблицу нечетных
            conn.commit()
cursor.execute('''SELECT *FROM BAZ1''')
z = cursor.fetchall()
print(z)
q=len(z) # узнаем длину таблицы 1

cursor.execute('''SELECT *FROM BAZ2''')
z = cursor.fetchall()
print(z)
d=len(z) # узнаем длину таблицы 2

if d > 5: # проверяем больше ли длинна второй таблицы
    cursor.execute('''DELETE FROM BAZ1 WHERE id = 1''')
    conn.commit()
else:
    cursor.execute('''UPDATE BAZ1 SET col1='Hello' WHERE id=1''')
    conn.commit()

cursor.execute('''SELECT *FROM BAZ1''')
k=cursor.fetchall()
print(k)

cursor.execute('''SELECT *FROM BAZ2''')
k=cursor.fetchall()
print(k)
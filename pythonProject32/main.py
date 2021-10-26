import sqlite3
conn=sqlite3.connect('q_1.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS TAB1(id INTEGER PRIMARY KEY AUTOINCREMENT, col1 INTEGER)''')

class A:
    def asw(self,a=None,b=None,c=None):
        if a is not None and b is None and c is None:
            cursor.execute('''INSERT INTO TAB1(col1) VALUES(3)''')
            conn.commit()
        elif a is not None and b is not None and c is None:
            if type(b) is int:
                print(3)
                cursor.execute('''DELETE FROM TAB1 WHERE id=2''')
                conn.commit()
        elif a is not None and b is not None and c is not None:
            if type(c) is int:
                cursor.execute('''UPDATE TAB1 SET col1=77 WHERE id =3''')
                conn.commit()

example=A()
example.asw(2,3,2)
cursor.execute('''SELECT *FROM TAB1''')
z=cursor.fetchall()
print(z)

#elif a is not None and b is not None and c is None:
#if type(b) is int:
 #   print(3)
  #  cursor.execute('''DELETE FROM TAB1 WHERE ID=1''')
   # conn.commit()
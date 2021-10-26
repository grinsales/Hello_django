import sqlite3
conn = sqlite3.connect("sql_1.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book (book_id INTEGER PRIMARY KEY AUTOINCREMENT, 
 title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), amount INT)''' )
cursor.execute('''INSERT into book(title,author,price,amount) VALUES('Python','A.S.Pushkin',25.00, 5)''')
conn.commit()
cursor.execute('''SELECT*FROM book''')
k = cursor.fetchall()
print(k)
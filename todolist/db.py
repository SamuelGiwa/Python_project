import sqlite3

conn = sqlite3.connect(r'todolist\todo.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
INSERT INTO users (name)
VALUES (?)
''', ('Alice',))  

cursor.execute('''
INSERT INTO users (name)
VALUES (?)
''', ('Bob',))  

conn.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
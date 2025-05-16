import sqlite3

conn = sqlite3.connect('filmes.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE filmes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        genero TEXT NOT NULL,
        nota INTEGER
    )             
''')

conn.commit()
conn.close()
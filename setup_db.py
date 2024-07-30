import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Cria a tabela user_info com o id de cada cliente e suas infos
c.execute('''
    CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        familia BIT NOT NULL,
        terror BIT NOT NULL,
        classico BIT NOT NULL
    )
''')

conn.commit()
conn.close()

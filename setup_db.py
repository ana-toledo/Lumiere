import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Cria a tabela user_emails com os emails e seus ids
c.execute('''
    CREATE TABLE IF NOT EXISTS user_emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

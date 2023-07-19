import sqlite3

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email_address TEXT)''')

records = [( 'Camila', 'Sandoval', 'c@gmail.com'),
           ( 'Aaron', 'Agosto', 'c@gmail.com'),
           ( 'Sergio', 'Colmenares', 'c@gmail.com'),
           ( 'Ilan', 'Vaks', 'c@gmail.com'),
           ( 'Sarah', 'Kuss', 'c@gmail.com'),]


cursor.executemany('''INSERT INTO Users(first_name, last_name, email_address) VALUES (?, ?, ?)''', records)
cursor.execute('''SELECT * FROM Users''')
print(cursor.fetchall())

cursor.execute('SELECT Email FROM Users')
print(cursor.fetchall())

conn.commit()
conn.close()
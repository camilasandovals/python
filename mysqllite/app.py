import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
              (Title TEXT, Director TEXT, Year INT)''')


release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year =?", release_year)
print(cursor.fetchall())
# --------------------Add one fetch one 
# cursor.execute('''INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976)''')
# cursor.execute('''SELECT * FROM Movies''')
# print(cursor.fetchone())


# --------------------fetch multiple
# famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
#                ('Back to the Future', 'Robert Zemeckis', 1985),
#                ('Moontise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)
# cursor.execute('SELECT * FROM Movies')
# print(cursor.fetchall())
connection.commit()
connection.close()

#python3 -m  venv sqlalchemy-workspace
#cd sqlalchemy-workspace 
#source bin/activate
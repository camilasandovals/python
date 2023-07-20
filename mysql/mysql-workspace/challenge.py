import mysql.connector as mysql


def connect(db_name): 
  try:
    return mysql.connect(
      host="127.0.0.1",
      user="root",
      password="18222222",
      database=db_name
    )
  except Error as e:
    print(e)

def add_sale(cursor, sale):
  for item in sale:
    cursor.execute('INSERT INTO sales(item_name, price, ordered_by) VALUES(%s, %s, %s)', item )

def find_most_expensive(table):
  cursor.execute('SELECT * FROM {}'.format(table))
  records = cursor.fetchall()
  max = 0 
  for record in records:
    if record[2] > max:
      max = record[2]
  print(max)

def read(table):
    cursor.execute('SELECT * FROM {}'.format(table))
    records = cursor.fetchall()
    print(records)

if __name__ == '__main__':
  db = connect('Red30')
  cursor = db.cursor()

  sale = [["tea", 1, "sergio"], ["coffee", 2, "jiho"], ["shoes", 40, "sandra"], ["car", 500, "olger"]]

  # add_sale(cursor, sale)
  # read("sales")
  find_most_expensive("sales")
  
  db.commit()
  db.close()



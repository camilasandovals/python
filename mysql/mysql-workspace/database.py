import mysql.connector as mysql

def connect(db_name):
  try:
    return mysql.connect(
      host="127.0.0.1",
      user="root",
      password="18222222",
      database=db_name)
  except Error as e:
    print(e)

def add_project(cursor, project_title, project_description, tasks):
  project_data = (project_title, project_description)
  cursor.execute('''INSERT INTO projects(title, description)
                 VALUES (%s, %s)''', project_data)
  tasks_data = []
  for task in tasks:
    task_data = (cursor.lastrowid, task)
    tasks_data.append(task_data)
  cursor.executemany('''INSERT INTO tasks(project_id, description)
                     VALUES(%s, %s)''', tasks_data)

if __name__ == '__main__':
  db = connect("python_db")

  cursor = db.cursor()

  tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
  add_project(cursor, "Clean house", "Clean house by room", tasks)
  db.commit()

  cursor.execute("SELECT * FROM projects")
  records = cursor.fetchall()
  print(records)

  cursor.execute("SELECT * FROM tasks")
  records = cursor.fetchall()
  print(records)

  db.close()
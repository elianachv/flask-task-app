from server.services import user

def get_tasks_by_user(user_id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM tasks WHERE user = %s', [user_id])
  db_tasks = cur.fetchall()
  tasks = []
  for task in db_tasks:
    assignee = user.get_user_by_id(task[1])
    status = get_status_by_id(task[5])
    final_task = task + (assignee[1], status[0],)
    tasks.append(final_task)
  cur.close()
  return tasks

def get_all_status():
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM statuses')
  statuses = cur.fetchall()
  cur.close()
  return statuses

def get_status_by_id(status_id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT status FROM statuses WHERE id = %s', [status_id])
  status = cur.fetchone()
  cur.close()
  return status

def add_task(title, description, deadline, user_id, status_id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('INSERT INTO tasks (user, title, description, date, status) VALUES(%s,%s,%s,%s,%s)', [user_id,title, description, deadline, status_id])
  mysql.connection.commit()
  cur.close()
  return

def edit_task(task_id,title, description, deadline, user_id, status_id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('UPDATE tasks SET user = %s, title = %s, description = %s, date = %s, status = %s WHERE id = %s', [user_id,title, description, deadline, status_id,task_id])
  mysql.connection.commit()
  cur.close()
  return

def delete_task(task_id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('DELETE FROM tasks WHERE id = %s', [task_id])
  mysql.connection.commit()
  cur.close()
  return

def done(task_id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('UPDATE tasks SET status = 4 WHERE id = %s', [task_id])
  mysql.connection.commit()
  cur.close()
  return
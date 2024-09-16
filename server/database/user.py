
def get_user_by_email_and_password(email, password):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM users WHERE email = %s AND password = %s', [email, password])
  user = cur.fetchone()
  cur.close()
  return user

def get_user_by_email(email):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM users WHERE email = %s', [email])
  user = cur.fetchone()
  role = get_user_role(user[5])
  final_user= user + (role[0],)
  cur.close()
  return final_user

def get_user_role(role_id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT name FROM roles WHERE id = %s', [role_id])
  role = cur.fetchone()
  cur.close()
  return role

def get_user_by_id(id):
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM users WHERE id = %s', [id])
  user = cur.fetchone()
  role = get_user_role(user[5])
  final_user = user + (role[0],)
  cur.close()
  return final_user

def get_all():
  from server import mysql
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM users')
  final_users = []
  db_users = cur.fetchall()
  
  for db_user in db_users:
    role = get_user_role(db_user[5])
    final_user = db_user + (role[0],)
    final_users.append(final_user)
  
  cur.close()
  return final_users
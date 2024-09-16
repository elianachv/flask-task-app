
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
  cur.close()
  return user
from server.database import user
from flask import session, render_template, redirect, url_for

def register(name, lastname, email, password, password_confirmation):
  db_user = user.get_user_by_email(email=email)
  
  if password == password_confirmation:
    if db_user is not None:
      return render_template('register.html', message = '⚠️ Ya tienes una cuenta inicia sesión.')
    else:
      user.register(name, lastname, email, password)
      return redirect(url_for('login'))

  else:
    return render_template('register.html', message = '⚠️ Las contraseñas no coinciden')


def login(email, password):
  db_user = user.get_user_by_email(email=email)
  
  if db_user is not None:

    if db_user[2] == password:
      session['id'] = db_user[0]
      session['email'] = email
      session['name'] = db_user[3]
      session['lastname'] = db_user[4]
      session['role'] = db_user[6]
      return redirect(url_for('tasks'))
    
    else:
      return render_template('index.html', message = '⚠️ Credenciales incorrectas. Por favor, intenta de nuevo.')

  else:
    return render_template('index.html', message = '⚠️ Lo sentimos, no tienes una cuenta. ¡Registrate!')
  
def logout():
 session.clear()
 return redirect(url_for('home'))  

def get_user_by_id(user_id):
 return user.get_user_by_id(user_id)

def get_all():
 return user.get_all()  
from server.database import user
from flask import session, render_template, redirect, url_for

def login(email, password):
  db_user = user.get_user_by_email(email=email)
  print(db_user)
  
  if db_user is not None:

    if db_user[2] == password:
      session['email'] = email
      session['name'] = db_user[3]
      session['lasname'] = db_user[4]
      return redirect(url_for('tasks'))
    
    else:
      return render_template('index.html', message = '⚠️ Credenciales incorrectas. Por favor, intenta de nuevo.')

  else:
    return render_template('index.html', message = '⚠️ Lo sentimos, no tienes una cuenta. ¡Registrate!')
  


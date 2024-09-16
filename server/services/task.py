from server.database import task
from server.services import user
from flask import session, render_template, redirect, url_for

def show_home():
  if session:
      tasks = get_tasks(session['id'])
      users = user.get_all()
      return render_template('tasks.html', tasks = tasks, users = users)
  else:
    return render_template('index.html', message = '⚠️ Debes iniciar sesión')

def get_tasks(user_id):
   return task.get_tasks_by_user(user_id=user_id)

def add_task(title, description, deadline, user_id, status_id):
  task.add_task(title=title, description=description, deadline=deadline, user_id=user_id, status_id=status_id)
  return redirect(url_for('tasks'))

def edit_task(task_id,title, description, deadline, user_id, status_id):
  task.edit_task(task_id=task_id,title=title, description=description, deadline=deadline, user_id=user_id, status_id=status_id)
  return redirect(url_for('tasks'))

def delete_task(task_id):
  task.delete_task(task_id=task_id)
  return redirect(url_for('tasks'))

def done(task_id):
  task.done(task_id=task_id)
  return redirect(url_for('tasks'))


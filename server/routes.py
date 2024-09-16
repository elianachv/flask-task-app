from flask import render_template, request, session
from server.services import user, task

def user_routes(app):

  @app.route('/', methods=['GET'])
  def home():
    return render_template('index.html')

  @app.route('/login', methods=['POST'])
  def login():
    email = request.form['email']
    password = request.form['password']
    return user.login(email=email, password=password)
  
  @app.route('/logout', methods=['GET'])
  def logout():
    return user.logout()

def task_routes(app):
  @app.route('/tasks',  methods=['GET'])
  def tasks():
    return task.show_home()
  
  @app.route('/task/add',  methods=['POST'])
  def add_task():
    title = request.form['title']
    description = request.form['description']
    deadline = request.form['deadline']
    user_id = request.form['user']
    status_id = request.form['status']
    return task.add_task(title=title, description=description, deadline=deadline, user_id=user_id, status_id=status_id)
  
  @app.route('/task/edit',  methods=['POST'])
  def edit_task():
    task_id = request.form['task_id']
    title = request.form['title']
    description = request.form['description']
    deadline = request.form['deadline']
    user_id = request.form['user']
    status_id = request.form['status']
    return task.edit_task(task_id=task_id, title=title, description=description, deadline=deadline, user_id=user_id, status_id=status_id)
 
  @app.route('/task/delete',  methods=['POST'])
  def delete_task():
    task_id = request.form['task_id']
    return task.delete_task(task_id=task_id)
  
  @app.route('/task/done',  methods=['POST'])
  def done_task():
    task_id = request.form['task_id']
    return task.done(task_id=task_id)
 
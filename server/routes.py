from flask import render_template, request, session
from server.services import user, task

def user_routes(app):

  @app.route('/', methods=['GET'])
  def home():
    return render_template('index.html')

  @app.route('/login', methods=['GET'])
  def login():
    return render_template('login.html')
  
  @app.route('/login', methods=['POST'])
  def login_user():
    email = request.form['email']
    password = request.form['password']
    return user.login(email=email, password=password)
  
  @app.route('/logout', methods=['GET'])
  def logout():
    return user.logout()
  
  @app.route('/register', methods=['GET'])
  def register():
    return render_template('register.html')
  
  @app.route('/user', methods=['POST'])
  def add_user():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    password_confirmation= request.form['password_confirmation']
    file = request.files
    photo = file["photo"]
    return user.register(name=name,lastname=lastname,email=email,password=password, password_confirmation = password_confirmation, photo = photo)

def task_routes(app):
  @app.route('/tasks',  methods=['GET'])
  def tasks():
    return task.show_home()
  
  @app.route('/task/add',  methods=['POST'])
  def add_task():
    title = request.form['title']
    description = request.form['description']
    deadline = request.form['deadline']
    status_id = request.form['status']
    role = session['role']
    if role == 'EMPLOYEE':
      user_id = session['id']
    else:
      user_id = request.form['user']
    return task.add_task(title=title, description=description, deadline=deadline, user_id=user_id, status_id=status_id)
  
  @app.route('/task/edit',  methods=['POST'])
  def edit_task():
    task_id = request.form['task_id']
    title = request.form['title']
    description = request.form['description']
    deadline = request.form['deadline']
    status_id = request.form['status']
    role = session['role']
    if role == 'EMPLOYEE':
      user_id = session['id']
    else:
      user_id = request.form['user']
    return task.edit_task(task_id=task_id, title=title, description=description, deadline=deadline, user_id=user_id, status_id=status_id)
 
  @app.route('/task/delete',  methods=['POST'])
  def delete_task():
    task_id = request.form['task_id']
    return task.delete_task(task_id=task_id)
  
  @app.route('/task/done',  methods=['POST'])
  def done_task():
    task_id = request.form['task_id']
    return task.done(task_id=task_id)
 
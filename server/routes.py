from flask import render_template, request
from server.services import user

def user_routes(app):

  @app.route('/', methods=['GET'])
  def home():
    return render_template('index.html')

  @app.route('/login', methods=['POST'])
  def login():
    email = request.form['email']
    password = request.form['password']
    return user.login(email=email, password=password)

def task_routes(app):
  @app.route('/tasks',  methods=['GET'])
  def tasks():
    return "tasks"
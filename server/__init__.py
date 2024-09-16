from flask import Flask
from flask_mysqldb import MySQL
from server.routes import user_routes, task_routes
from server import config

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # Inicializa conexion con la base de datos
    app.config['SECRET_KEY'] = config.HEX_SEC_KEY
    app.config['MYSQL_HOST'] = config.MYSQL_HOST
    app.config['MYSQL_USER'] = config.MYSQL_USER
    app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
    app.config['MYSQL_DB'] = config.MYSQL_DB

    mysql.init_app(app)

    # Inicializa rutas
    user_routes(app)
    task_routes(app)

    return app

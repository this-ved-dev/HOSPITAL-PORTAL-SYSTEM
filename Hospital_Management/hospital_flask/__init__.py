from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


app = Flask(__name__)

app.config['SECRET_KEY'] = '1c80f8b14d90e45d697cfec6524a0ac9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
from hospital_flask import routes
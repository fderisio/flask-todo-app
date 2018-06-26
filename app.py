from flask import Flask
from flask_migrate import Migrate
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_todo_app.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')  # this line is called: decorator
def hello_world():
    return 'Hello, World!'


# import string
# import random

from flask import Flask
from flask_migrate import Migrate
# from models import ToDoItem, ToDoList
from urls import todo_list_api
from views import ToDoListListView,ToDoListGetUpdateDelete

from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_todo_app.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# ejecutan las funciones dentro del blueprint todo_list_api, en todos los prefijos que quieras
app.register_blueprint(todo_list_api, url_prefix='/todo-list')
app.register_blueprint(todo_list_api, url_prefix='/todo-item')


# Past examples:

# def random_string(l):
#     letter = string.ascii_letters
#     return ''.join(random.choice(letter) for i in range(l))

# @app.cli.command()
# def create_dummy_data():
#     for i in range(10):
#         new_todo_list = ToDoList(name=f'My new list: {random_string(20)}')
#         for j in range(10):
#             new_item = ToDoItem(
#                 content=f'My new todo item: {random_string(5)}',
#                 todo_list=new_todo_list
#             )
#             db.session.add(new_item)
#     db.session.commit()
#
#
# @app.cli.command()
# def give_word():
#     print(random_string(10))

# @app.route('/<username>')
# def hello(username):  # username can now be used as arg
#     return f'Hi: {username}'

# @app.route('/', methods=['GET', 'POST'])  # this line is called: decorator
# def hello_world():
#     if request.method == 'POST':  # imported from flask.request
#         print(f'------------ DATA =>{request.data} ------------')
#     todo_lists = ToDoList.query.filter_by(id=1)  #ToDoList is the class of the table
#     return json.dumps(f'{[l.serialize() for l in todo_lists]}')

# request.__dict__
# request.data --> JSON
# request.query_string


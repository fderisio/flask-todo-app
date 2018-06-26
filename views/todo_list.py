from flask import request, abort
import json

from flask.views import MethodView

from models import ToDoList
from views.helpers import APIView

# Class to list all lists
# method view allows the methods written (si se intenta get something, sin def get, da error)


class ToDoListListView(MethodView):
    def get(self):
        todo_lists = ToDoList.query.filter_all
        return json.dumps(f'{[l.serialize() for l in todo_lists]}')


# class to get/update/delete from a single list
class ToDoListGetUpdateDelete(APIView):
    def get(self, **kwargs): # method view allows the methods written (si se intenta get something, sin def get
        # self.session
        todo_list_id = kwargs.get('todo_list_id')
        todo_list = ToDoList.query.filter_by(id=todo_list_id)
        if not todo_list:
            return abort(401, f'ToDo List with ID{todo_list_id} was not found')
        return json.dumps(f'{[todo_list.serialize() for l in todo_list]}')

    # def post(self, **kwargs):
    #     todo_lists = ToDoList.query.filter_by(id=1)
    #     return json.dumps(f'{[l.serialize() for l in todo_lists]}')

    def delete(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        todo_list = ToDoList.query.filter_by(id=todo_list_id)
        return json.dumps(f'{[l.serialize() for l in todo_list]}')

    def patch(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        todo_list = ToDoList.query.filter_by(id=todo_list_id)
        return json.dumps(f'{[l.serialize() for l in todo_list]}')

# @app.route('/todo-list/<todo_list_id>/', methods=['GET'])
# def get_todo_items(todo_list_id):

# @app.route('/todo-list/all/', methods=['GET'])
# def get_all_lists():
#     todo_lists = ToDoList.query.all
#     return json.dumps(f'{[l.serialize() for l in todo_lists]}')

# @app.route('/todo-list/new/', methods=['POST'])
# def add_new_list():
#     todo_lists = ToDoList.query.filter_by(id=1)
#     return json.dumps(f'{[l.serialize() for l in todo_lists]}')

# @app.route('/todo-list/update/<todo_list_id>', methods=['PATCH'])
# def update(todo_list_id):
#     todo_lists = ToDoList.query.filter_by(id=1)
#     return json.dumps(f'{[l.serialize() for l in todo_lists]}')

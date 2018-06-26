# First Class: to list all lists
# method view allows the methods written inside (si se intenta get something, sin def get, da error)
# Second Class: to get/update/delete from a single list
from flask import abort, request
import json
from flask.views import MethodView
from models import ToDoList, ToDoItem
from views.helpers import APIView


class ToDoListListView(MethodView):
    def get(self):
        todo_lists = ToDoList.query.all()
        return json.dumps(f'{[l.serialize() for l in todo_lists]}')



class ToDoListGetUpdateDelete(APIView):
    def get(self, **kwargs):
        data = request.data
        print(data)
        # self.session  # to update delete or add only
        todo_list_id = kwargs.get('todo_list_id')
        todo_list = ToDoList.query.filter_by(id=todo_list_id).first()
        if not todo_list:
            return abort(401, f'ToDo List with ID{todo_list_id} was not found')
        return json.dumps(f'{[l.serialize() for l in todo_list.todos]}')

    def delete(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        todo_list = ToDoList.query.filter_by(id=todo_list_id).first()
        return json.dumps(f'{[l.serialize() for l in todo_list]}')

    def patch(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        todo_list = ToDoList.query.filter_by(id=todo_list_id)
        return json.dumps(f'{[l.serialize() for l in todo_list]}')

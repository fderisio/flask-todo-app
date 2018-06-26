from flask import Blueprint

from views.todo_list import ToDoListListView, ToDoListGetUpdateDelete

todo_list_api = Blueprint('todo_list_api', 'todo_list_api')

todo_list_api.add_url_rule(
    rule='/all',
    view_func=ToDoListListView.as_view('view_all_lists')
)

todo_list_api.add_url_rule(
    rule='/new',
    view_func=ToDoListGetUpdateDelete.as_view('get-update-delete-list')
)

todo_list_api.add_url_rule(
    rule='/update/<todo_list_id>',
    view_func=ToDoListGetUpdateDelete.as_view('get-update-delete-list')
)

todo_list_api.add_url_rule(
    rule='/delete/<todo_list_id>',
    view_func=ToDoListGetUpdateDelete.as_view('get-update-delete-list')
)

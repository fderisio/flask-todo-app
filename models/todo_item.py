from datetime import datetime
from database import db


class ToDoItem(db.Model):
    __tablename__ = 'todo_item'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))  # 255 characters
    created = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime.utcnow
    )
    todo_list_id = db.Column(
        db.Integer,
        db.ForeignKey('todo_list.id'),  # Todo_list (table name). id (field)
        nullable=False
    )
    todo_list = db.relationship(
        'TodoList',
        backref=db.backref('todos', lazy=True)  # si no es lazy da error
    )
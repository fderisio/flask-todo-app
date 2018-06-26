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
    due_date = db.Column(
        db.DateTime,
        nullable=True
    )
    done_flag = db.Column(
        db.Boolean,
        default=False
        # db.Boolean.create_constraint=False
    )
    todo_list_id = db.Column(
        db.Integer,
        db.ForeignKey('todo_list.id'),  # todo_list (table name). id (field)
        nullable=False

    )
    todo_list = db.relationship(
        'ToDoList',
        backref=db.backref('todos', lazy=True, cascade='all, delete-orphan')  # si no es lazy da error
    )

    def serialize(self):
        if self.__getattribute__('due_date'):
            return {
                'id': self.id,
                'content': self.content,
                'created': self.created.strftime('%d, %b, %Y'),
                'due_date': self.due_date.strftime('%d, %b, %Y'),
                'done_flag': self.done_flag,
                'todo_list_id': self.todo_list_id
            }
        else:
            return {
                'id': self.id,
                'content': self.content,
                'created': self.created.strftime('%d, %b, %Y'),
                'done_flag': self.done_flag,
                'todo_list_id': self.todo_list_id
            }
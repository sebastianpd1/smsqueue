from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Queue:

    def __init__(self):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, item):

        self._queue.append(item)

    def dequeue(self):
        if self._mode == 'FIFO':
            item = self._queue.pop(0)
            return item["phone"]
        else:
            item = self._queue.pop(-1)
            return item["phone"]

    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue)



class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }
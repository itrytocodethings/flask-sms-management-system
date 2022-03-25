from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

# class Queue:
#     def __init__(self):
#         self._queue = []
#         # depending on the _mode, the queue has to behave like a FIFO or LIFO
#         self._mode = 'FIFO'
#     # def enqueue(self, item):
#     # def dequeue(self):
#     # def get_queue(self):
#     # def size(self):
#         return len(self._queue) 
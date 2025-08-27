from datetime import datetime, timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<User {self.email}>'

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(20), default='Medium')
    created_at = db.Column(db.DateTime, default=func.now())
    due_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Task {self.title}>'



    def get_due_date(self):
        if self.due_date:
            return self.due_date.strftime('%Y-%m-%d %H:%M')
        return "No due date"

    def is_overdue(self):
        if self.due_date and not self.completed:
            return self.due_date < datetime.now(timezone.utc)
        return False

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    from .models import Task
    filter_type = request.args.get('filter', 'all')
    task_query = Task.query.filter_by(user_id=current_user.id)

    if filter_type == 'active':
        tasks = task_query.filter_by(completed=False).all()
    elif filter_type == 'completed':
        tasks = task_query.filter_by(completed=True).all()
    else:
        tasks = task_query.all()

    return render_template("home.html", 
                           user=current_user,
                           tasks=tasks,
                           filter_type=filter_type)

@views.route('/add-task', methods=['POST'])
@login_required
def add_task():
    from . import db
    from . models import Task

    title = request.form.get('title')
    if not title:
        flash('Task title cannot be empty.', category='error')
    else:
        new_task=Task(title=title,
                user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully.', category='success')
    return redirect(url_for('views.home'))

@views.route('/delete-task/<int:task_id>')
@login_required
def delete_task(task_id):
    from . import db
    from . models import Task

    task = Task.query.get(task_id)

    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted!', category='success')
    else:
        flash('Permission denied', category='success')
    return redirect(url_for('views.home'))

@views.route('/toggle-task/<int:task_id>')
@login_required
def toggle_task(task_id):
    from . import db
    from . models import Task
    task = Task.query.get(task_id)

    if task and task.user_id == current_user.id:
        task.completed = not task.completed
        db.session.commit()

        if task.completed:
            flash('Task marked as completed!', category='success')
        else:
            flash('Task marked as active!', category='success')
    else:
        flash('Task not found!', category='error')
    return redirect(url_for('views.home'))
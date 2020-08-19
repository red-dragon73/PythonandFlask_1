from flask import render_template, redirect, url_for, flash, get_flashed_messages
from app import my_app, db
from datetime import datetime
from models import Tasks

import forms


@my_app.route('/')
@my_app.route('/index')
def index():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)


@my_app.route('/add', methods=['GET', 'post'])
def add():
    form = forms.AddText()
    if form.validate_on_submit():
        t = Tasks(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash("Task successfully added")
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


@my_app.route('/edit/<int:task_id>', methods=['get', 'post'])
def edit(task_id):
    task = Tasks.query.get(task_id)
    form = forms.AddText()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task has been updated")
            return redirect(url_for('index'))

        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    return redirect(url_for('index'))


@my_app.route('/delete/<int:task_id>', methods=['get','post'])
def delete(task_id):
    task = Tasks.query.get(task_id)
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted.')
            return redirect(url_for('index'))

        return render_template('delete.html', form=form, task_id=task_id, title=task.title)

    return redirect(url_for('index'))
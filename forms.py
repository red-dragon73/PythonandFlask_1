from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddText(FlaskForm):
    title = StringField(label="Task: ", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class DeleteTaskForm(FlaskForm):
    submit = SubmitField(label='Delete')

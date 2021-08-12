from flask_wtf import FlaskForm
from recapp.models import User, Storage, Ticket
from wtforms.validators import DataRequired, ValidationError
from wtforms import StringField, IntegerField, PasswordField, SubmitField, FloatField


class Login(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    login = SubmitField('login')

    def validate_username(self, username):
        user_validated = User.query.filter_by(username=username.data).first()
        if not user_validated:
            raise ValidationError("This user doesn't exist")


class Head(FlaskForm):
    name = StringField(validators=[DataRequired()])
    add = SubmitField('continue')


class Generator(FlaskForm):
    item_name = StringField(validators=[DataRequired()])
    item_quantity = IntegerField(validators=[DataRequired()])
    unit_price = FloatField(validators=[DataRequired()])
    add = SubmitField('+')


class Search(FlaskForm):
    search_bar = StringField(validators=[DataRequired()])
    search_action = SubmitField('O')

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, user_check):
        user = User.query.filter_by(username = user_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
        
    def validate_email(self, email_check):
        email_add = User.query.filter_by(email = email_check.data).first()
        if email_add:
            raise ValidationError('Email address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2,max=30),DataRequired()])
    email = StringField(label='Emai Address:', validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[DataRequired()]) 
    password = PasswordField(label='Password: ', validators=[DataRequired()])

    submit = SubmitField(label='Login')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
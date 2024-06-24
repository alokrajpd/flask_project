from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SelectField,
                    PasswordField,
                     SubmitField,
                    BooleanField,
                    DateField
                     )

from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    equal_to
)
class SignupForm(FlaskForm):
    username = StringField(
        "username",
        validators=[DataRequired(),Length(2,30)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired() , Email()]
    )
    gender = SelectField("Gender",
                         choices = ["Male" , "Female" , "Other"],
                         validators=[Optional()])
    dob = DateField("DOB",
                    validators=[Optional()])
    password = PasswordField("Password" ,
                             validators=[DataRequired() ,Length(5,25)])
    confirm_password = PasswordField("Confirm Password",
                             validators=[DataRequired(), Length(5, 25),equal_to("password")])

    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(5, 25)])
    remember_me=BooleanField("Remember Me")

    submit = SubmitField("Sign up")
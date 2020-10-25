from flask_wtf import FlaskForm
from wtforms.widgets.html5 import NumberInput
import pymongo
from os import getenv
from wtforms import (
    StringField,
    IntegerField,
    TextAreaField,
    PasswordField,
    BooleanField,
    SubmitField,
    HiddenField,
    RadioField,
    SelectField,
)
from wtforms.validators import DataRequired

myclient = pymongo.MongoClient(getenv("MONGODB_URI"))

sn = myclient["shasnotes"]
mesechtos = sn["meseches"]
user_notes = sn["UserNotes"]
ms = mesechtos.find({"$query": {}, "$orderby": {"itemNum": 1}})
mesechtos = [(m["name"], m["hebName"]) for m in ms]


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


class AddNoteForm(FlaskForm):
    category = HiddenField()
    meseches = SelectField("מסכת", choices=mesechtos)
    daf = IntegerField("דף", widget=NumberInput())
    sugya = StringField("סוגיא:", validators=[DataRequired()])
    relates_to = SelectField(
        u"Relates to", choices=[("gemara", "גמרא"), ("rashi", 'רש"י'), ("tosafos", "תוס")]
    )
    starting_phrase = StringField("דיבור המתחיל:")
    public = BooleanField("לתועלת הרבים", default=True)
    content = TextAreaField(u"תוכן:")
    submit = SubmitField("שמור")

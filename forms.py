from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ChatForm(FlaskForm):
    chat = StringField("Chat")
    submit = SubmitField("Send")

class InboxForm(FlaskForm):
    svar = StringField("Svar")
    submit = SubmitField("Send")
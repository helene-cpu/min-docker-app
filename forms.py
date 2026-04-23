from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ChatForm(FlaskForm):
    chat = StringField("Chat")
    submit = SubmitField("Send")
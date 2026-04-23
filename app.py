from flask import Flask, render_template, session, redirect
import mysql.connector
from forms import ChatForm

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/read", methods=["POST", "GET"])
def read():
    form = ChatForm()
    if form.validate_on_submit():
        chat = form.chat.data

        if user:
            return redirect("/virus")
        else:
            return "Wrong"

    return render_template('read.html', form = form)

@app.route("/virus", methods=["POST", "GET"])
def virus():
    return render_template("virus.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
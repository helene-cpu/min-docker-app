from flask import Flask, render_template, session, redirect, jsonify
from forms import ChatForm, InboxForm
import sqlite3
import requests
from datetime import datetime, timedelta


app = Flask(__name__)
app.secret_key = "secretkey"

def init_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Passord (ID INTEGER AUTOINCREMENT PRIMARY KEY, Passord TEXT)""")

    cursor.execute("SELECT COUNT(*) FROM Passord")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""INSERT INTO Passord (Passord) VALUES (?)""", ("max",))
    conn.commit()
    conn.close()

def get_current_time(timezone="Europe/Oslo"):
    url = f"https://timeapi.io/api/Time/current/zone?timeZone={timezone}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data["dateTime"]

    except Exception as e:
        print("Error fetching time:", e)
        return None

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/read", methods=["POST", "GET"])
def read():
    form = ChatForm()
    if form.validate_on_submit():
        chat = form.chat.data

        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Passord WHERE Passord = ?",  (chat,))
        user = cursor.fetchone()

        conn.commit()
        conn.close()

        if user:
            return redirect("/virus")
        else:
            return "Wrong"

    return render_template('read.html', form = form)

@app.route("/virus", methods=["POST", "GET"])
def virus():
    current_time = get_current_time()

    current_time = datetime.fromisoformat(current_time)

    end_time = current_time + timedelta(minutes=10)

    return render_template("virus.html", end_time=end_time.isoformat())

@app.route("/inbox", methods=["POST", "GET"])
def inbox():
    form = InboxForm()
    if form.validate_on_submit():
        svar = form.svar.data.strip().lower()
        if svar == "maria" or svar == "maria hansen":
          svar = form.svar.data.strip().lower()
        if svar in ["maria", "maria hansen"]:
            session["gåte1_løst"] = True  # husk at gåten er løst
            return render_template("inbox.html", form=form, riktig=True)
        else:
            return render_template("inbox.html", form=form, feil=True)
    return render_template("inbox.html", form = form)


@app.route("/staff")
def staff():
    return render_template("staff.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
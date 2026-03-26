from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/read")
def read():
    return render_template('read.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
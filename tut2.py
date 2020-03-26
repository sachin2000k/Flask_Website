from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/sachin")
def sachin():
    return "kya haal chaal bro "

@app.route("/boot")
def about():

    return render_template('boot.html')
app.run(debug=True)
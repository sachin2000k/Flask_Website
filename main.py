from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('config.json','r') as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
app.config
db = SQLAlchemy(app)
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
print(db_connection)
#this class defines the columns of database
class Contact(db.Model):

    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), unique = False, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    ph_num = db.Column(db.String(15), nullable=False)
    mess = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    return render_template('index.html', params = params)



@app.route('/about')
def about():
    return render_template('about.html', params = params)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('NAME')
        email = request.form.get('EMAIL')
        message = request.form.get('MESSAGE')
        ph_num = request.form.get('PHONENO')


        entry = Contact(Name = name, email = email, mess = message, ph_num = ph_num)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html', params = params)

@app.route('/post')
def post():
    return render_template('post.html', params = params)

app.run(debug=True)
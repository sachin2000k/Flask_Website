from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#import json
#with open('config.json','r') as c:
 #   params = json.load(c)["params"]

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/ai website'
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
    Name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    ph_num = db.Column(db.String(15), nullable=False)
    mess = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')

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

    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')
@app.route('/abc')
def abc():
    return "hello mahima"
app.run(debug=True)
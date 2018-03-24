from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'regdb')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email = :email"
    query2 = "SELECT * FROM users WHERE password = :password"
    hashed_password = md5.new(request.form['password']).hexdigest()
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': request.form['email'],
             'password': hashed_password
           }
    # Run query,
    exists = mysql.query_db(query, data)
    pwd = mysql.query_db(query2, data)
    
    if len(exists) == 1 and len(pwd) == 1:
        flash("user logged in!")
        return render_template('success.html')
    elif len(exists) == 1 and len(pwd) != 1:
        flash("incorrect password")
    elif len(exists) != 1 and len(pwd) == 1:
        flash("user name not recognized")
    else:
        flash("We're sorry please register below")

    return redirect('/')



@app.route('/register', methods=['POST'])
def register():
    print "recieved registration"
    query = "SELECT * FROM users WHERE email = :email"
    hashed_password = md5.new(request.form['password']).hexdigest()
    data = {
             'email': request.form['email'],
             #'password': request.form['password'],
             #'cpassword': request.form['cpassword']
             'password': hashed_password
           }
    password = request.form['password']
    cpassword = request.form['cpassword']
    user = request.form['email']
    exists = mysql.query_db(query, data)
    if len(exists) == 1:
        flash("username already in use")
    elif len(exists) == 0 and password == cpassword and len(user) > 3:
        query = "INSERT INTO users(email, password, created_at, updated_at) values(:email, :password, now(), now())"
        flash("successfully registered!")
        mysql.query_db(query, data)
        return render_template('success.html')
    elif len(user) < 3:
        flash("Please enter a valid email address")
    else:
        flash("passwords don't match!")

    return redirect('/')

app.run(debug=True)
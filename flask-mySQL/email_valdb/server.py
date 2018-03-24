from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'emaildb')
@app.route('/')
def index():
    query = "SELECT * FROM user_emails"
    emails = mysql.query_db(query)
    print emails  
    return render_template('index.html', all_emails=emails)


@app.route('/validate', methods=['POST'])
def validate():
    query = "SELECT * FROM user_emails WHERE email = :email"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': request.form['email'],
           }
    # Run query, 
    exists = mysql.query_db(query, data)
    if len(exists) == 1:
        flash("Sorry this address is already in use")
    elif len('email') > 3:
        query = "insert into user_emails(email, created_at) values(:email, now())"
        data = {
            'email': request.form['email']
        }
        flash("Email accepted")
        mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
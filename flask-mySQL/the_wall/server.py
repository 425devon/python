from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'walldb')
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
        session['first_name'] = mysql.query_db("SELECT first_name FROM users WHERE email = :email", data)[0]['first_name']
        session['user_id'] = mysql.query_db("SELECT id FROM users WHERE email = :email", data)[0]['id']
        return redirect('/postPop')
    elif len(exists) == 1 and len(pwd) != 1:
        flash("incorrect password")
    elif len(exists) != 1 and len(pwd) == 1:
        flash("user name not recognized")
    else:
        flash("User not recognized please register below")

    return redirect('/')



@app.route('/register', methods=['POST'])
def register():
    print "recieved registration"
    query = "SELECT * FROM users WHERE email = :email"
    hashed_password = md5.new(request.form['password']).hexdigest()
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_password
           }
    password = request.form['password']
    cpassword = request.form['cpassword']
    user = request.form['email']
    exists = mysql.query_db(query, data)
    if len(exists) == 1:
        flash("username already in use")
    elif len(exists) == 0 and password == cpassword and len(user) > 3:
        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) values(:first_name, :last_name, :email, :password, now(), now())"
        flash("successfully registered!")
        mysql.query_db(query, data)
        session['first_name'] = mysql.query_db("SELECT first_name FROM users WHERE email = :email", data)[0]['first_name']
        session['user_id'] = mysql.query_db("SELECT id FROM users WHERE email = :email", data)[0]['id']
        return redirect('/postPop')
    elif len(user) < 3:
        flash("Please enter a valid email address")
    else:
        flash("passwords don't match!")

    return redirect('/')

@app.route('/post', methods=['POST'])
def getpost():
    data = {
        'message':request.form['message'],
        'user_id': session['user_id']
    }
    if len(request.form['message']) > 1:
        query = "INSERT INTO messages(user_id, message, created_at, updated_at) values(:user_id, :message, now(), now())"
        mysql.query_db(query, data)
    

    return redirect('/postPop')

@app.route('/postPop', methods=['GET','POST'])
def postPop():
    query = """SELECT concat(users.first_name, " ", users.last_name) as user_name, date_format(messages.created_at, "%M %D %Y") as post_at, messages.message, messages.id
    FROM messages
    join users on messages.user_id = users.id"""
    posts = mysql.query_db(query)

    queryC = """SELECT concat(users.first_name, " ", users.last_name) as com_name, date_format(comments.created_at, "%M %D %Y") as com_at, comments.comment, comments.message_id
    from comments
    join users on comments.users_id = users.id"""
    comments = mysql.query_db(queryC)

    return render_template('success.html', all_posts=posts, all_comments=comments)

@app.route('/pcomment', methods=['GET','POST'])
def postComment():
    data = {
        'message_id': int(request.form['action']),
        'user_id': session['user_id'],
        'comment': request.form['comment']
    }
    if len(request.form['comment']) > 1:
        query = "INSERT INTO comments(message_id, users_id, comment, created_at, updated_at) values(:message_id, :user_id, :comment, now(), now())"
        mysql.query_db(query, data)
        return redirect('/postPop')

@app.route('/logout', methods=['GET','POST'])
def clearSession():
    session.pop('first_name')
    session.pop('user_id')
    return redirect('/')

app.run(debug=True)
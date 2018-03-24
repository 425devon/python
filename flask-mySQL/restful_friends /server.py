from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "select id, concat(first_name, ' ', last_name) as full_name, email, date_format(created_at, '%M %D %Y') as created_at, updated_at from friends"
    friends = mysql.query_db(query)  
    return render_template('index.html', all_friends=friends)

@app.route('/newUser')
def newuser():

    return render_template('new_user.html')



@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"

    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }

    mysql.query_db(query, data)
    return redirect('/')

@app.route('/show/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('show.html', friend=friends[0])

@app.route('/edit/<friend_id>')
def edit(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)

    return render_template('edit_user.html', friend=friends[0])

@app.route('/update/<friend_id>', methods=['GET','POST'])
def update(friend_id):
    query = """UPDATE friends
    SET first_name = :first_name, last_name = :last_name, email = :email
    WHERE id = :specific_id"""

    data = {
        'specific_id': friend_id,
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'email': request.form['email'],
    }

    mysql.query_db(query, data)

    return redirect('/')

@app.route('/remove/<friend_id>', methods=['GET','POST'])
def removeUser(friend_id):
    query = """Delete FROM friends
    WHERE id = :specific_id"""

    data = {'specific_id': friend_id}

    mysql.query_db(query, data)

    return redirect('/')


app.run(debug=True)
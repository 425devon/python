from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/validate', methods=["POST"])
def submit_survey():
    session['email'] = request.form['email']
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['password'] = request.form['password']
    session['cpassword'] = request.form['cpassword']

    if len(session['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    if any(char.isdigit() for char in session['fname']):
        flash("Name cannot be empty or contain numbers!")
        return redirect('/')
    if len(session['fname'])< 1:
        flash("Name cannot be empty or contain numbers!")
        return redirect('/')
    if any(char.isdigit() for char in session['lname']):
        flash("Name cannot be empty or contain numbers!")
        return redirect('/')
    if len(session['lname'])< 1:
        flash("Name cannot be empty or contain numbers!")
        return redirect('/')
    if len(session['password'])< 8:
        flash("Password must be atleast 8 characters")
        return redirect('/')
    if session['password'] != session['cpassword']:
        flash("Passwords do not match!")
        return redirect('/')

    return "Thank You for registering {}!".format(session['fname'])
    


app.run(debug=True) # run our server
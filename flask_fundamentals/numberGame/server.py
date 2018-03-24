from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

randomNum = random.randrange(0,101)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/guess', methods =['POST'])
def getguess():
    session.pop('answer', None)
    session.pop('user', None)
    if request.form['guess'] > str(0):
        session['user'] = request.form['guess']
        return redirect('/logic')
    else:
        session['answer'] = "I'm sorry I didn't understand"
        return redirect('/')

@app.route('/logic')
def analyze():
    global randomNum
    print randomNum
    if session['user'] < str(randomNum):
        session['answer'] = "Too low!"
        session.pop('user', None)
    elif session['user'] > str(randomNum):
        session['answer'] = "Too high!"
        session.pop('user', None)
    else:
        session['answer'] = "Wow are you telepathic?! Play Again?"
        session.pop('user', None)
    return redirect('/')





app.run(debug=True)
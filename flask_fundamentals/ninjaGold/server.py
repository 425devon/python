from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
casinoNum = random.randrange(-51,51)
farmNum = random.randrange(9,21)
cavNum = random.randrange(4,11)
houseNum = random.randrange(1,6)
#session['alog'] = ""

@app.route('/')
def index():
    if 'alog' not in session:
        session['alog'] = "Welcome to ninja gold!"
    return render_template("index.html")

@app.route('/money', methods =['POST'])
def getMoney():
    print "got some money"
    if 'gold' not in session:
        session['gold'] = 0
    else:
        if request.form['building'] == 'farm':
            farmNum = random.randrange(9,21)
            session['gold'] += farmNum
            session['alog'] += ("\n earned {} gold from the farm!").format(farmNum)
        elif request.form['building'] == 'cave':
            cavNum = random.randrange(4,11)
            session['gold'] += cavNum
            session['alog'] += ("\n You found {} gold in the cave!").format(cavNum)
            print session['gold']
        elif request.form['building'] == 'house':
            houseNum = random.randrange(1,6)
            session['gold'] += houseNum
            session['alog'] += ("\n earned {} gold from the house!").format(houseNum)
            print session['gold']
        elif request.form['building'] == 'casino':
            casinoNum = random.randrange(-51,51)
            session['alog'] += ("\n Tested your luck at the casino, {}").format(casinoNum)
            session['gold'] += casinoNum
            print session['gold']

    return redirect('/')
    '''
    elif request.form['building'] == 'house':
        pass
    elif request.form['building'] == 'casino':
        pass
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
'''
app.run(debug=True)
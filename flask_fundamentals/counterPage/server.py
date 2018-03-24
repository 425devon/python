from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
counter = 0

@app.route('/', methods=['GET'])
def addCounter():
  global counter
  counter += 1
  session['counter'] = counter

  return render_template('index.html')

@app.route('/add', methods=['POST'])
def countTwo():
  global counter
  counter += 1
  return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
  global counter
  counter = 0
  return redirect('/')


app.run(debug=True)
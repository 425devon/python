from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/left')
def left():
  return render_template('left.html')

@app.route('/right')
def right():
  return render_template

app.run(debug=True) # run our server

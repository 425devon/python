from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
    print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
    name = request.form['name']
    print name
   # redirects back to the '/' route
    return redirect('/')

app.run(debug=True) # run our server
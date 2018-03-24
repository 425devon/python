from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   name = request.form['name']
   email = request.form['email']

   print "Got Post Info name: {}, email: {}".format(name,email)
   # redirects back to the '/' route
   return render_template('success.html')
app.run(debug=True) # run our server
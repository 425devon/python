from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=["POST"])
def submit_survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
  
    
    if len(session['name']) < 1:
        # display validation errors
        flash("Name cannot be empty!")
        return redirect('/')
    if len(session['comment']) < 1:
        flash("Please leave a comment")
    elif len(session['comment']) > 120:
        flash("Please make comment shorter than 120 characters")
        return redirect('/')
    return render_template('result.html')


app.run(debug=True) # run our server
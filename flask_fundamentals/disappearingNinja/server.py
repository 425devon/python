from flask import Flask, render_template  
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                          
def landing():
    return render_template('index.html')

@app.route('/ninjas')
def call_ninja():
    return render_template('ninja.html')

@app.route('/ninjas/blue')
def call_blue():
    return render_template('blue.html')

@app.route('/ninjas/orange')
def call_orange():
    return render_template('orange.html')

@app.route('/ninjas/red')
def call_red():
    return render_template('red.html')

@app.route('/ninjas/purple')
def call_purple():
    return render_template('purple.html')

@app.route('/ninjas/black')
def call_black():
    return render_template('april.html')

@app.route('/ninjas/123')
def call_nin():
    return render_template('april.html')

                                     
                                          
                                          
    
app.run(debug=True)       
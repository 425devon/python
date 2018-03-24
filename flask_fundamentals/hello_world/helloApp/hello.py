from flask import Flask, render_template  
app = Flask(__name__)    
                        
@app.route('/')         
                         
                        
@app.route('/success')
def success():
  return render_template('success.html')


app.run(debug=True)      # Run the app in debug mode.

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
    
        

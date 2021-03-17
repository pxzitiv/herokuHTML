from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return ('Welcome !')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/login')
def login():
    return render_template('login.html')

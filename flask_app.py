from flask import Flask, render_template
app = Flask(__name__)

<html>
  <head>  
  </head>
  <style>
  body {background-color: #3CB371;
  font-family: Comic Sans MS;
  font-size: 80%;}
  </style>
  <body>
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/login')
def login():
    return render_template('login.html')
    </body>
    </head>
        

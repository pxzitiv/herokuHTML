from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_Alexander():
    return render_templates('first.html')

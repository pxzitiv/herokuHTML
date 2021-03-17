from flask import Flask, render_templates
app = Flask(__name__)

@app.route('/')
def hello_Alexander():
    return render_templates ("first.html")

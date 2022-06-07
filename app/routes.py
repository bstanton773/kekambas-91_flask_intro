from app import app
from flask import render_template

@app.route("/")
def index():
    user_dict = {
        'username': 'brians',
        'email': 'brians@codingtemple.com'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user_dict, colors=colors)


@app.route('/signup')
def signup():
    return render_template('signup.html')
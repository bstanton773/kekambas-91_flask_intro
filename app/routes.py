from app import app
from flask import render_template
from app.forms import SignUpForm

@app.route("/")
def index():
    user_dict = {
        'username': 'brians',
        'email': 'brians@codingtemple.com'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user_dict, colors=colors)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('HELLO THIS WAS A HUGE SUCCESS!')
    return render_template('signup.html', form=form)
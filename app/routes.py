from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
from app.models import Post, User

@app.route("/")
def index():
    user_dict = {
        'username': 'brians',
        'email': 'brians@codingtemple.com'
    }
    posts = Post.query.all()
    return render_template('index.html', user=user_dict, posts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Get the data from the form fields
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # Query the User table for any users with username/email from form
        user_check = User.query.filter((User.email == email)|(User.username == username)).all()
        if user_check:
            flash('A user with that username and/or email already exists. Please try again.', 'danger')
            return redirect(url_for('signup'))

        # Add the user to the database
        new_user = User(email=email, username=username, password=password)

        # Show message of success/failure
        flash(f'{new_user.username} has successfully signed up!', 'success')
        # redirect back to the homepage
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)
from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, PostForm
from app.models import Post, User
from random import randint

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

        # Show message of success
        flash(f'{new_user.username} has successfully signed up!', 'success')
        # redirect back to the homepage
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


@app.route('/create-post', methods=["GET", "POST"])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Get data from the form
        post_title = form.title.data
        post_body = form.body.data
        user_id = randint(1,5)
        # Add new post to database with form info
        new_post = Post(title=post_title, body=post_body, user_id=user_id)
        # Flash a success message to the user
        flash(f'{new_post.title} has been created', 'success')
        # Return to the home page
        return redirect(url_for('index'))

    return render_template('create_post.html', form=form)
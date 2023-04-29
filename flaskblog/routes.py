from flask import render_template, url_for, flash, redirect
from flaskblog import app
from .forms import (
    RegistrationForm,
    LoginForm
)
from .models import User, Post


posts = [
    {
        'author': 'Oğuzhan Öksel',
        'title': 'An Title',
        'content': 'an content about nothing',
        'date_posted': 'April 29, 2023',
    },
    {
        'author': 'Elfo',
        'title': 'Hi I\'m Elfo',
        'content': 'an content about Elfo',
        'date_posted': 'November 19, 2022',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@example.com' and form.password.data == '123456':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
